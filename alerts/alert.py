#!/usr/bin/python
#
# Save as /etc/munin/scripts/alert.py
# chown munin:munin /etc/munin/scripts/alert.py
# chmod +x /etc/munin/scripts/alert.py
#

import sys
import os
import json

def humanreadable( jsonalert ):
  hascritical = (len(jsonalert['critical']) > 0)
  haswarning  = (len(jsonalert['warning'])  > 0)
  hasunknown  = (len(jsonalert['unknown'])  > 0)

  report = ""

  if hascritical:
    for i in jsonalert['critical']:
      report += "CRITICAL: {0} {1}: {2}={3}".format(jsonalert['host'],
                       jsonalert['graph_title'], i['label'],i['value'])

  if haswarning:
    for i in jsonalert['warning']:
      report += "WARNING: {0} {1}: {2}={3}".format(jsonalert['host'],
                       jsonalert['graph_title'], i['label'],i['value'])

  if hasunknown:
    for i in jsonalert['unknown']:
      report += "UNKNOWN: {0} {1}: {2}={3}".format(jsonalert['host'],
                       jsonalert['graph_title'], i['label'],i['value'])

  if hascritical + haswarning + hasunknown == 0:
    report += "OK: {0} {1}".format(jsonalert['host'],jsonalert['graph_title'])

  return report

for line in sys.stdin:
  j = json.loads(line)
  readable = humanreadable(j)
  print readable