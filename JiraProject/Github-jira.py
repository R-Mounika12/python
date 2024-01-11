from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJiraIssue():
    url = "https://team-pcwcr7ne.atlassian.net/rest/api/3/issue"
    # GET the token from Jira Account "/profile/manage Account/security/create and manage API tokens"
    API_TOKEN = <taken>

    auth = HTTPBasicAuth("<emailID>", API_TOKEN)

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
        #board click on elipses, configure board, issue types, and select the issue
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
