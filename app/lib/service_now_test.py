import json
import os
import requests
import sys

class ServiceNowTest(object):

    def __init__(self):
        pass

    def create_incident(self, event):
        servicenow_instance = "",
        short_description="",
        snow_api_user_id = os.getenv("SNOW_USERNAME")
        snow_api_password = os.getenv("SNOW_PASSWORD")
        API_ok = [200, 201]

        url = "https://%s.service-now.com/api/now/table/incident" % servicenow_instance

        headers = {"Content-Type":"application/json","Accept":"application/json"}

        incident_title = "Halo Security Event: %s" % event["name"]

        request_body = {
            "incident_title": incident_title,
            "short_description": event["message"]
        }

        result=999

        while result not in API_ok:
            # HTTP request
            try:
                reply = requests.post(url,
                                      auth=(snow_api_user_id, snow_api_password),
                                      headers=headers,
                                      data=json.dumps(request_body)
                                     )
                result = reply.status_code

                # Check HTTP status code.  If not 200 or 201, then do...
                if reply.status_code not in API_ok:
                    print('Status:', reply.status_code, 'Headers:', reply.headers, 'Error Response:',reply.json())
                    exit()
            except requests.exceptions.RequestException as e:
                print e
                sys.exit(1)

        '''
        # Show the reply.
        print('Status: %s\n' % reply.status_code)
        print('Headers: %s\n' % reply.headers)
        print('Response: %s\n' % json.dumps(reply.json(), indent = 2, sort_keys = True))
        '''

        return reply