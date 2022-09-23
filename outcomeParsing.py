import json
import os
import openai

with open('key.txt', 'r') as f:
    OPENAI_API_KEY = f.read()
    
def GPT_Answer(query, text):
    ## Call the API key under your account (in a secure way)
    openai.api_key = OPENAI_API_KEY
    response = openai.Answer.create(
    engine="text-davinci-002",
    prompt =  query+'\nTranscript: '+text+'\nResolution: ',
    temperature = 0.4,
    top_p = 1,
    max_tokens = 64,
    frequency_penalty = 0.5,
    presence_penalty = 0
    )
    return print(response.choices[0].text)

casetexts = json.load(open('cases_with_text.json', 'r'))
for case in casetexts:    
    text = case['full_text']
    query = "Decide whether a court transcript's resolution is a conviction, an acquittal, or neither. Think step by step."
    res = GPT_Answer(query, text)
    case['resolution'] = res
    print("Case", case['title'], ": ", res)
    input("Continue?")

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
