import json

casetexts = json.load(open('cases_with_text.json', 'r'))
alltexts = ""
textlist = []
for case in casetexts:
    alltexts += case['full_text']+ "\n"
    textlist.append(case['full_text'])

#---------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# nltk basic imports and downloads
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

#load in the NTLK stopwords to remove articles, preposition and other words that are not actionable
from nltk.corpus import stopwords
# This allows to create individual objects from a bog of words
from nltk.tokenize import word_tokenize
# Lemmatizer helps to reduce words to the base form
from nltk.stem import WordNetLemmatizer
# Ngrams allows to group words in common pairs or trigrams..etc
from nltk import ngrams
from nltk import Counter

import seaborn as sns

def word_frequency(sentences):
# joins all the sentenses
    sentence = ' '.join(sentences)
    # creates tokens, creates lower class, removes numbers and lemmatizes the words
    new_tokens = word_tokenize(sentence)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens =[t for t in new_tokens if t not in stopwords.words('english')]
    new_tokens = [t for t in new_tokens if t.isalpha()]
    lemmatizer = WordNetLemmatizer()
    new_tokens =[lemmatizer.lemmatize(t) for t in new_tokens]
    #counts the words, pairs and trigrams
    counted = Counter(new_tokens)
    counted_2= Counter(ngrams(new_tokens,2))
    counted_3= Counter(ngrams(new_tokens,3))
    #creates 3 data frames and returns thems
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
    trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
    return word_freq,word_pairs,trigrams

freq, bi, tri = word_frequency(textlist)
print(freq.head(10))
print()
print(bi.head(10))
print()
print(tri.head(10))
print()

input("Continue to seaborn plots?")
numResult = int(input("How many results do you want to plot?"))
# create subplot of the different data frames
fig, axes = plt.subplots(3,1,figsize=(8,20))
sns.barplot(ax=axes[0],x='frequency',y='word',data=freq.head(numResult))
sns.barplot(ax=axes[1],x='frequency',y='pairs',data=bi.head(numResult))
sns.barplot(ax=axes[2],x='frequency',y='trigrams',data=tri.head(numResult))
plt.show()