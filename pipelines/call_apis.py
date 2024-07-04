import requests
import json
from util import get_session

# TODO: Replace the official URLs
URL_MAP = {
    "get-domain-urls": "https://api.instill.tech/v1beta/users/chunhao094/pipelines/get-domain-urls/trigger",
    "crawler": "https://api.instill.tech/v1beta/users/chunhao094/pipelines/crawler/trigger",
    "summary": "https://api.instill.tech/v1beta/users/chunhao094/pipelines/summary/trigger",
    "craft-cold-email-pipeline": "https://api.instill.tech/v1beta/users/chunhao094/pipelines/craft-cold-emial/trigger",
    "send-email": "https://api.instill.tech/v1beta/users/chunhao094/pipelines/send-email/trigger"
}

def call_api(pipeline_name, data):
    url = URL_MAP[pipeline_name]
    json_data = json.dumps(data)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_session("auth_token")}'
    }
    response = requests.post(url, headers=headers, data=json_data)
    return response.json()