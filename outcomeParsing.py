import json
import os
import openai
from gtts import gTTS
from playsound import playsound

language = 'en'

# def saveAndSpeak(response):
#     myobj = gTTS(text=response, lang=language, slow=False)
#     myobj.save("output.mp3")
#     playsound('output.mp3')
#     os.remove("output.mp3")


with open('key.txt', 'r') as f:
    OPENAI_API_KEY = f.read()
    
def GPT_Answer(query, text):
    ## Call the API key under your account (in a secure way)
    openai.api_key = OPENAI_API_KEY
    ## Set the parameters for the API call
    parameters = {
        #"engine": "text-davinci-002",
        "engine": "text-curie-001",
        #"prompt": query+'\nTranscript: '+text+'\nResolution: ',
        "prompt": query+'\nTranscript: '+text+'\nThoughts: ',
        #"prompt": query+'\nTranscript: '+text+'\nThoughts? ',
        "max_tokens": 64,
        "temperature": 0.4,
        "top_p": 1,
        "frequency_penalty": 0.5,
        "presence_penalty": 0
    }
    response = openai.Completion.create(**parameters)
    #print(response.choices[0].text)
    return response.choices[0].text

casetexts = json.load(open('cases_with_text.json', 'r'))
for i, case in enumerate(casetexts):    
    sample_text = case['full_text'][:1000] + case['full_text'][-1000:]
    # Ask gpt3 to determine whether dress was a factor in the case
    #query = "Did the victim's dress or clothes come up in the case? Answer with yes, maybe, or no."
    #query = "Decide whether the transcript's resolution is a conviction, an acquittal, or neither. Think step by step and reply in one word."
    query = "Is the victim's dress mentioned? Reply with yes or no."
    res = GPT_Answer(query, sample_text)
    case['resolution'] = res
    
    #saveAndSpeak(res)
    print("Case", case['title'], ": ", res)

#--------------------------------
# Old approach:
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
