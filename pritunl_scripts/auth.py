import os
import sys
import json
import time
import uuid
import hmac
import logging
import base64
import urllib3
import hashlib
import requests

BASE_URL = os.environ['PRITUNL_BASE_URL']
API_TOKEN = os.environ['PRITUNL_API_TOKEN']
API_SECRET = os.environ['PRITUNL_API_SECRET']


def auth_request(method, path):
    auth_timestamp = str(int(time.time()))
    auth_nonce = uuid.uuid4().hex
    auth_string = '&'.join([API_TOKEN, auth_timestamp, auth_nonce, method.upper(), path])
    auth_signature = base64.b64encode(hmac.new(
    API_SECRET.encode('utf-8'), auth_string.encode('utf-8'), hashlib.sha256).digest())

    auth_headers = {
        'Auth-Token': API_TOKEN,
        'Auth-Timestamp': auth_timestamp,
        'Auth-Nonce': auth_nonce,
        'Auth-Signature': auth_signature,
        'Content-Type': 'application/json'
    }
    return auth_headers


# Function to call the API, template is optional
def request(method, path, template=None):
    try:
        return requests.request(method, BASE_URL + path,
            headers=auth_request(method, path), 
            verify=True, data=json.dumps(template)
        )
    except Exception as e:
        logging.warning(e)
