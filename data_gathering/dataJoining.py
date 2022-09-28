import json

cases = json.load(open('stored_data/cases_with_text_1k.json', 'r'))
cases1k = cases[:1000]
cases2k3k = json.load(open('stored_data/cases_with_text_2k3k.json', 'r'))
cases4k5k = json.load(open('stored_data/cases_with_text_4k5k.json', 'r'))

#print("Cases1:", len(cases1k)) # 1000
#print("Cases2:", len(cases2k3k)) # 2000
#print("Cases3:", len(cases4k5k)) # 2308

casesFull = cases1k + cases2k3k + cases4k5k
print("Number of Cases:", len(casesFull)) # 5308

with open('casetexts_all.json', 'w') as f:
    json.dump(casesFull, f)