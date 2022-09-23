import json

casetexts = json.load(open('cases_with_text.json', 'r'))
convited_keys = ['convicted', 'sentenced to']
acquited_keys = ['acquitted', 'not guilty', 'dismissed', 'thrown out']
cases = []

outcomes = {'convicted': 0, 'acquitted': 0, 'unknown': 0}
for case in casetexts:
    
    text = case['full_text'].lower()
    case['outcome'] = 'unknown'
    if any(key in text for key in convited_keys):
        case['outcome'] = 'convicted'
        outcomes['convicted'] += 1
    if any(key in text for key in acquited_keys):
        if(case['outcome'] == 'convicted'):
            case['outcome'] = 'unknown'
            outcomes['unknown'] += 1
            outcomes['convicted'] -= 1
        else:
            case['outcome'] = 'acquitted'
            outcomes['acquitted'] += 1
    else:
        if(case['outcome'] != 'convicted'):
            case['outcome'] = 'unknown'
            outcomes['unknown'] += 1
    cases.append(case)

print(outcomes)
cases.insert(0, outcomes)

with open('cases_with_outcome.json', 'w') as f:
    json.dump(cases, f)    
