import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint


headers = {"User-Agent": "I am a student srivenkatesh.subramaniam@student.sl.on.ca"}


cik = "0000320193"


url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, features="xml")


print(response)

pprint(response.json())
