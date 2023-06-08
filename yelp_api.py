"""Interact with the Yelp API"""

import os 
import requests 
import json 
from pprint import pprint 


url = f"https://api.yelp.com/v3/businesses/search?location=San%20Francisco&term=pop-up&limit=50"
headers = {
    "accept": "application/json", 
    "Authorization": f"Bearer {os.environ['YELP_API_KEY']}"
    } 


response = requests.get(url, headers=headers) 

pprint(json.loads(response.text))

