import requests
import json
import os
"""
Get SLACK Webhook URL from Environment Varibles
"""
url = os.environ.get('SLACK_URL', None)

def post_to_slack(message):
    """ Result will be published to Slack Channel
    """
    payload = {"text": message}
    requests.post(url, data={"payload": json.dumps(payload)})

    