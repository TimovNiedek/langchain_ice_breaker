import requests
import os
import json

PROFILE_ID = 'timo-van-niedek'

api_key = os.environ['PROXYCURL_API_KEY']
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': f'https://linkedin.com/in/{PROFILE_ID}/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)
print(response.json())

# Save to json file
with open(f'data/linkedin/{PROFILE_ID}.json', 'w') as f:
    json.dump(response.json(), f, indent=4)