import quarantine
import lib

# Build config
config = quarantine.ConfigHelper()

# Halo object
halo = quarantine.HaloGeneral(config)

# Halo events
events = quarantine.HaloEvents(config)

# Matcher object
matcher = quarantine.Matcher(config.match_list)

# jira = lib.JiraController()
snow = lib.ServiceNowTest()

# Iterate over events, quarantine targeted workloads

while True:
    for event in events:
        if matcher.is_a_match(event["type"]):
            # print "Quarantining workload: %s" % event["server_id"]
            # jira.create_ticket(event)
            snow.create_incident(event)
            # halo.quarantine_workload(event["server_id"])
