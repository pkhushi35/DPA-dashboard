import requests
import json
from datetime import datetime

API_KEY = '7f4aa8c51b6b7e017fbfeb3d136dd7b9205b076e38e355e325dcde2b551148f5'
headers = {'X-OTX-API-KEY': API_KEY}
url = 'https://otx.alienvault.com/api/v1/indicators/export'

def fetch_otx_data():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.text
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(f"otx_data_{timestamp}.json", "w") as f:
            f.write(data)
        print("Data saved.")
    else:
        print("Error:", response.status_code)

fetch_otx_data()