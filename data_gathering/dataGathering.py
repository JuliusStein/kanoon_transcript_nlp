import requests
from urllib.parse import urljoin
from datetime import datetime
from kanoon.indianKanoon import IndianKanoon
import json
from bs4 import BeautifulSoup

k = IndianKanoon()
cases = []
tids = []
numPagesToSearch = int(input("How many pages of cases do you want to search?\n"))
queryToSearch = input("What is the query you want to search?\n") + " doctypes: judgments"

# Search for different queries about clothing & sexual assault
# only add to cases if the tid is not already in tids
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
    if ((i+1)%100 == 0):
      print("Writing to file")
      with open('cases.json', 'w') as f:
        json.dump(cases, f)

#Write the cases to a file
with open('casesAll.json', 'w') as f:
  json.dump(cases, f)