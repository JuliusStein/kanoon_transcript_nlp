import json
import nltk
import sys

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
#sentences = nltk.sent_tokenize(alltexts)
sentences = alltexts.split('.')

print("Sentences loaded, analyzing...")

#---------------
toConsider = []
keywords = ["wearing", "dress", "jeans", "top", "skirt", "shirt", "sari", "saree", 
            "sador", "riha", "shalwar", "choli", "kurta", "pants", "blouse", 
            "shorts", "coat","sweater"]
for sentence in sentences:
    contains_keyword = any(keyword in sentence.lower() for keyword in keywords)
    if contains_keyword:
        toConsider.append(sentence)

print("Sentences filtered, writing...")
#toConsider = list(set(toConsider))

# Write to file
import pandas as pd
pd.DataFrame(toConsider).to_csv("filtered_sentences.csv")
#pd.DataFrame(toConsider).to_excel("filtered_sentences.xlsx")
#pd.DataFrame(toConsider).to_json("filtered_sentences.json")

with open("filtered_sentences.txt", "w") as f:
    for sentence in toConsider:
        f.write(str(sentence.encode(sys.stdout.encoding, errors='replace')))
        f.write("\n")