import requests
import json
import urllib3

# Suppress warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_GET_AUTH_headers():
    d1 = {}
    d1['username'] = 'SystemBatch'
    d1['password'] = 'Axiom#1234'
    d1['Accept'] = 'application/json'
    d1['Content-Type'] = 'text/plain'
    return d1

def get_POST_AUTH_headers():
    d1 = {}
    d1['username'] = 'SystemBatch'
    d1['password'] = 'Axiom#1234'
    d1['Accept'] = 'application/json'
    d1['Content-Type'] = 'text/plain'
    return d1

url = 'https://gbrdsr000007101.intranet.barcapint.com:8083/cv/data/pr_BOE_VARIANCE/Variance_And_Trend/dm_BOE_BT_TRENDS_REPORT_DATA_new/instance'

response = requests.get(url, headers=get_GET_AUTH_headers(), verify=False)

if response.status_code == 200:
    data = response.json()
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
