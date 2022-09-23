import requests
from urllib.parse import urljoin
from datetime import datetime
from kanoon.indianKanoon import IndianKanoon
import json
from bs4 import BeautifulSoup

k = IndianKanoon()
OPENAI_API_KEY = "sk-y22uQeOCmvLN03icAMj2dLVpJwZjvyu6u2F69nbt"
cases = []
tids = []
numPagesToSearch = int(input("How many pages of cases do you want to search?\n"))
queryToSearch = input("What is the query you want to search?\n") + " doctypes: judgments"
# Search for first X pages of sexual assault cases on Kanoon
for i in range(numPagesToSearch):
  resp = k.search(queryToSearch, i)
  #print(resp)
  #input("Continue?")  
  print("Page", i+1, "processed")
  for entry in resp['docs']:
    if entry['tid'] not in tids:
      case = {}
      case['title'] = entry['title']
      case['tid'] = entry['tid']
      case['court'] = entry['docsource']
      case['date'] = entry['publishdate']
      tids.append(entry['tid'])
      cases.append(case)

#Write the cases to a file
with open('cases.json', 'w') as f:
  json.dump(cases, f)


#Search for different queries about clothing & sexual assault
# only add to cases if the tid is not already in tids