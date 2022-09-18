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

# Search for first X pages of sexual assault cases on Kanoon
for i in range(numPagesToSearch):
  resp = k.search('sexual assault', i)
  print("Page", i, "processed")
  for entry in resp['docs']:
    case = {}
    case['title'] = entry['title']
    case['tid'] = entry['tid']
    tids.append(entry['tid'])
    cases.append(case)

#Write the cases to a file
with open('cases.json', 'w') as f:
  json.dump(cases, f)


#Search for different queries about clothing & sexual assault
# only add to cases if the tid is not already in tids