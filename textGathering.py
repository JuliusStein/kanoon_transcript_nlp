import requests
from urllib.parse import urljoin
from datetime import datetime
from kanoon.indianKanoon import IndianKanoon
import json
from bs4 import BeautifulSoup

k = IndianKanoon()


# Read the cases from file
cases = json.load(open('cases.json', 'r'))
#print(cases)

# Get the full text of each case
for case in cases:
  resp = k.doc(case['tid'])
  raw_html = resp['doc']
  soup = BeautifulSoup(raw_html, 'html.parser')
  pTags = soup.find_all('p')
  text = ((' '.join([" ".join(p.text.split()) for p in pTags])).replace('\n', ' ')).replace('\t', ' ')
  
  #print(text)
  try:
    case['judge'] = soup.find('div', {'class': 'doc_bench'}).text
  except:
    try:
      case['judge'] = soup.find('div', {'class': 'doc_author'}).text
    except:
      case['judge'] = 'unknown'
  
  case['full_text'] = text
 
  print("Case", case['title'], "processed")
  #input("Continue?")

#Write the case texts to a file
with open('cases_with_text.json', 'w') as f:
    json.dump(cases, f)