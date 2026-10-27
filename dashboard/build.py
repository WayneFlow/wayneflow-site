import json
V_SQL = """SELECT
  toString(person_id) AS visitor,
  min(timestamp) AS first_seen,
  max(timestamp) AS last_seen,
  argMin(properties.$device_type, timestamp) AS device,
  argMin(properties.$browser, timestamp) AS browser,
  argMin(properties.$geoip_country_name, timestamp) AS country,
  argMin(properties.$geoip_subdivision_1_name, timestamp) AS region,
  argMin(properties.$geoip_city_name, timestamp) AS city,
  argMin(properties.$geoip_postal_code, timestamp) AS postal_code,
  coalesce(argMinIf(properties.wf_first_source, timestamp, properties.wf_first_source IS NOT NULL), nullIf(argMin(properties.$referring_domain, timestamp), '$direct'), 'direct') AS source,
  coalesce(argMinIf(properties.wf_first_channel, timestamp, properties.wf_first_channel IS NOT NULL), if(argMin(properties.$referring_domain, timestamp) = '$direct', 'direct', 'referral')) AS channel,
  argMin(properties.$pathname, timestamp) AS landing_page,
  countIf(event = '$pageview') AS pages_viewed,
  uniq(properties.$session_id) AS visits,
  countIf(event = 'book_call_click') AS cta_clicks,
  maxIf(toFloat(properties.depth), event = 'wf_scroll') AS max_scroll,
  maxIf(toFloat(properties.active_seconds), event = 'wf_engaged') AS engaged_seconds,
  countIf(event = 'wf_outbound_click') AS link_clicks,
  max(person.properties.email) AS email
FROM events
WHERE timestamp >= now() - INTERVAL {{days}} DAY
  AND event IN ('$pageview', '$pageleave', 'wf_visit', 'book_call_click', 'wf_scroll', 'wf_engaged', 'wf_outbound_click', '$autocapture')
GROUP BY person_id
ORDER BY last_seen DESC
LIMIT 500"""
P_SQL = """SELECT
  if(endsWith(properties.$pathname, 'index.html'), substring(properties.$pathname, 1, length(properties.$pathname) - 10), properties.$pathname) AS page,
  countIf(event = '$pageview') AS views,
  uniqIf(person_id, event = '$pageview') AS page_visitors,
  countIf(event = 'book_call_click') AS cta_clicks,
  uniqIf(person_id, event = 'book_call_click') AS clickers
FROM events
WHERE timestamp >= now() - INTERVAL {{days}} DAY
  AND event IN ('$pageview', 'book_call_click')
GROUP BY page
ORDER BY views DESC
LIMIT 50"""
A_SQL = """SELECT
  toString(uuid) AS id,
  timestamp AS at,
  toString(person_id) AS visitor,
  event,
  properties.$pathname AS page,
  coalesce(properties.label, properties.question, properties.section, toString(properties.depth), toString(properties.active_seconds), '') AS detail,
  coalesce(properties.wf_source, '') AS source,
  properties.$device_type AS device,
  properties.$geoip_country_name AS country,
  properties.$geoip_city_name AS city
FROM events
WHERE timestamp >= now() - INTERVAL 7 DAY
  AND event IN ('$pageview', 'book_call_click', 'wf_visit', 'wf_outbound_click', 'wf_scroll', 'wf_engaged', 'wf_faq_open', 'wf_screenshot_zoom', 'email_click', 'wf_contact_click', 'wf_calculator_use')
ORDER BY timestamp DESC
LIMIT 200"""
def src(sql, why, rules=None):
    cmd = 'call --json execute-sql ' + json.dumps({"query": sql, "context": why})
    return {"kind": "query", "connector": "PostHog", "tool": "exec",
            "args": {"command": cmd, "context": "Loading website visitor data for the site owner's live visitor dashboard.", "llm_model": "unknown"}, **({"rules": rules} if rules else {})}
docs = {
 "dash/meta": {"title": "WayneFlow Visitors"},
 "datasets/visitors": {"title": "Every visitor", "description": "One row per person who visited the website in the chosen period (7, 30 or 90 days): device, location, how they arrived, pages viewed and booking clicks. Reads PostHog events.", "source": src(V_SQL, "Per-visitor table for the visitor dashboard; governed catalog consulted: no match.", {"days": {"type": "number", "minimum": 1, "maximum": 365}})},
 "datasets/pages": {"title": "Pages and booking clicks", "description": "Views, visitors and Book a call clicks for each page of the website in the chosen period. Reads PostHog events.", "source": src(P_SQL, "Page performance for the visitor dashboard; governed catalog consulted: no match.", {"days": {"type": "number", "minimum": 1, "maximum": 365}})},
 "dash/params": {"days": 30},
 "datasets/activity": {"title": "Live activity, last 7 days", "description": "The latest 200 actions on the website: page views, arrivals, scrolls, booking clicks and link clicks. Reads PostHog events.", "source": src(A_SQL, "Recent activity feed for the visitor dashboard; governed catalog consulted: no match.")},
}
for k, v in docs.items():
    json.dump(v, open(k.replace('/', '__') + '.json', 'w'))
html = open('index.html').read()
json.dump({"text": html}, open('files__index.html.json', 'w'))
print('ok', len(html))
