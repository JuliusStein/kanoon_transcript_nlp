import json
import nltk

casetexts = json.load(open('./data_cleaning/northAcquit.json', 'r'))
print("JSON loaded...")
alltexts = ""
textlist = []
length = len(casetexts)
# for num,case in enumerate(casetexts):
#     if((num+1)%100 == 0):
#         print(num+1,"of",length,"cases loaded")
#     alltexts += case['full_text'] + "\n"
#     textlist.append(case['full_text'])
textlist = list(casetexts['full_text'].values())
alltexts = ' '.join(textlist)
sentences = nltk.sent_tokenize(alltexts)

print("Sentences loaded, analyzing...")

#---------------
toConsider = []
for sentence in sentences:
    if "obscene" in sentence.lower():
        toConsider.append(sentence)
    elif "indecent" in sentence.lower():
        toConsider.append(sentence)
    elif "provocative" in sentence.lower():
        toConsider.append(sentence)

print("Sentences filtered, printing...")

for sentence in toConsider:
    print(sentence)