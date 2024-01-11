from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(_name_)

def createJiraIssue():
    url = "https://team-pcwcr7ne.atlassian.net/rest/api/3/issue"
    API_TOKEN = "ATATT3xFfGF05Hu5SASQJGK6nbcP8wjeL2yzYWBMi3XCFs5yXnB_gC1QIIaZdcWcZjcipohPqOk8bBQCF8S9VzIaYkggC8mFWk63NZ1t0R9FH8oiuKIN0osZRrKHNsC5-_GrrVYAl_M3NVlUezmclTZysf9jxAzbPCJUpkWe6Ehw1QrL7yDs9Rc=9088A10D"

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
                "text": "My second jira ticket",
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
        "summary": "second ticket"
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run(host='0.0.0.0', port=5000)