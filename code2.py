import requests
import json
import urllib3

# Suppress warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_GET_AUTH_headers():
    headers = {
        'username': 'SystemBatch',
        'password': 'Axiom#1234',
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    return headers

# Function to extract required fields and format them as pipe-separated values
def process_data(data):
    rows = []
    
    for record in data.get('value', []):  # Iterate over each record in 'value'
        # Extract the required fields using double underscores
        instance_date = record.get('root__report_as_of_date', '')
        entity = record.get('root__entity', '')
        report_name = record.get('root__report_name', '')
        ordinatecodeX = record.get('root__ordinatecodex', '')
        ordinatecodeY = record.get('root__Ordinatecode', '')
        ordinatelabelZ = record.get('root__ORDINATELABELZ', 'null')  # Use 'null' if None
        amount = record.get('root__amount', '')

        # Combine report_name and ordinatecodes for the required format
        report_combined = f"{report_name}-{ordinatecodeY}-{ordinatecodeX}"
        
        # Format the fields into a pipe-separated row
        row = f"{instance_date}|{report_combined}|{ordinatelabelZ}|{entity}|{amount}"
        rows.append(row)
    
    return rows

# URL of the Axiom datamodel
url = 'https://gbrdsr000007101.intranet.barcapint.com:8083/cv/data/pr_BOE_VARIANCE/Variance_And_Trend/dm_BOE_BT_TRENDS_REPORT_DATA_new/instance'

# Get the data from the API
response = requests.get(url, headers=get_GET_AUTH_headers(), verify=False)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Process the data to extract and format the required fields
    formatted_data = process_data(data)
    
    # Write the formatted data to a .dat or .txt file
    with open('output.dat', 'w') as file:  # You can also use 'output.txt' if you prefer
        for line in formatted_data:
            file.write(line + '\n')  # Write each row to the file with a newline
    
    print("Data written to output.dat successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
