from tkinter import N
import requests
from urllib.parse import urljoin
from datetime import datetime
from kanoon.indianKanoon import IndianKanoon
import json
from bs4 import BeautifulSoup

k = IndianKanoon()


# Read the cases from file
cases = json.load(open('casesAll.json', 'r'))
#print(cases)
numCases = len(cases)
startNum = int(input("Enter the case number to start with: "))
toWrite = []
# Get the full text of each case
for i, case in enumerate(cases):
  if(i<startNum):
    continue
  else:
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
    toWrite.append(case)

    print("Case", i+1, "out of", numCases, "processed")
    if ((i+1)%1000 == 0):
        print("Writing to file")
        with open('cases_with_text.json', 'w') as f:
          json.dump(toWrite, f)
    #input("Continue?")
    
#Write the case texts to a file
with open('cases_with_text_toEnd.json', 'w') as f:
    json.dump(toWrite, f)