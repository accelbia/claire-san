import requests
import os
from pprint import pprint


TOKEN: str = os.getenv("AIRTABLE_TOKEN")

def get_data():
#     curl "https://api.airtable.com/v0/apphT7QAzpjDtBDHz/Dum%20Dum%20Projects?maxRecords=3&view=Grid%20view" \
#   -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"

    url = "https://api.airtable.com/v0/apphT7QAzpjDtBDHz/Dum%20Dum%20Projects?maxRecords=3&view=Grid%20view"
    headers = {
        'Authorization' : f'Bearer {TOKEN}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

if __name__ == '__main__':
    pprint(get_data())