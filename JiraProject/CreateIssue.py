# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://team-pcwcr7ne.atlassian.net/rest/api/3/issue"
API_TOKEN = "ATATT3xFfGF0MVd2Z3kS-PluE06Uz9mPHBrPqnQVXGQwEWN2Cx3Lkok2Bl6pNX20XojXwz3TPFP_9UySAebfEAYn3yJs6FPnfm3jBWxklnVk6atMnDNyNhIYvSK1KbCKh92TdCQ8uiL_6RkFoUWCXfcAbFCwyzJYWoPmX6QF9jVV66-iMgY8y-0=B99D3F61"

auth = HTTPBasicAuth("mounikareddappa12@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10005"
    },
    "project": {
      "key": "JP"
    },
    "summary": "first jira ticket"
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))