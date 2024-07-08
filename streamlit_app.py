import streamlit as st


#import nltk
#nltk.download('averaged_perceptron_tagger')

#from textblob import TextBlob
#from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# Define the functions
def wordcount(text):
    words = text.split()
    return len(words)

def lines(text):
    res = ""
    for i in text:
        if(i.isupper()):
            res+="*"+i
        else:
            res+=i
    m=res.split("*")
    m.remove('')
    numlines = len(m)
    return numlines

def type_token_ratio(text):
    words = text.split()
    unique_words = set(words)
    ttr = len(unique_words) / len(words) if words else 0
    return ttr

def ngrams(text, n):
    vectorizer = CountVectorizer(ngram_range=(n, n))
    analyzer = vectorizer.build_analyzer()
    n_grams = analyzer(text)
    return len(n_grams)

def unique_ngrams(text, n):
    vectorizer = CountVectorizer(ngram_range=(n, n))
    analyzer = vectorizer.build_analyzer()
    n_grams = analyzer(text)
    return len(set(n_grams))

def wordclass(text, category):
    blob = TextBlob(text)
    tags = blob.tags
    
    counts = {
        'adjective': 0,
        'noun': 0,
        'base_verb': 0,
        'total_verb': 0,
        'preposition': 0,
        'personal_pronoun': 0,
        'non3rdpersonsingularpresent_verb': 0,
        '3rdpersonsingularpresent_verb': 0,
        'past_participle_verb': 0,
        'coordinating_conjunctions': 0
    }
    
    for word, tag in tags:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
            counts['noun'] += 1
        elif tag == 'IN':
            counts['preposition'] += 1
        elif tag == 'VB':
            counts['base_verb'] += 1
            counts['total_verb'] += 1
        elif tag in ['VBD', 'VBG']:
            counts['total_verb'] += 1
        elif tag == 'VBN':
            counts['total_verb'] += 1
            counts['past_participle_verb'] += 1
        elif tag == 'VBP':
            counts['non3rdpersonsingularpresent_verb'] += 1
            counts['total_verb'] += 1
        elif tag == 'VBZ':
            counts['3rdpersonsingularpresent_verb'] += 1
            counts['total_verb'] += 1
        elif tag in ['JJ', 'JJR', 'JJS']:
            counts['adjective'] += 1
        elif tag == 'CC':
            counts['coordinating_conjunctions'] += 1
        elif tag == 'PRP':
            counts['personal_pronoun'] += 1
    
    content_density = (counts['total_verb'] + counts['noun'] + counts['adjective']) / wordcount(text)
    past_participle_verb_freq = counts['past_participle_verb'] / wordcount(text)
    coordinating_conjunctions_freq = counts['coordinating_conjunctions'] / wordcount(text)
    
    counts['content_density'] = content_density
    counts['past_participle_verb_freq'] = past_participle_verb_freq
    counts['coordinating_conjunctions_freq'] = coordinating_conjunctions_freq
    
    return counts[category]


st.write("Music Emotion Predictor")
# Input lyrics
lyrics = st.text_input("Please copy-paste the lyrics to your favourite song!")

percentage =  64
new_predictions = 4.5

import matplotlib.pyplot as plt


arousal_rating = percentage


fig, ax = plt.subplots(figsize=(10, 2))


sections = ['Low', 'Moderate', 'High']
colors = ['lightblue', 'lightgreen', 'orange']
positions = [0, 33.33, 66.66, 100]  #


for i in range(len(sections)):
    ax.barh(0, positions[i + 1] - positions[i], left=positions[i], color=colors[i], edgecolor='white', height=1.0)

#Needle
needle_position = arousal_rating
ax.plot([needle_position, needle_position], [-0.5, 0.5], color='black', linewidth=2)
ax.text(needle_position, 0.65, f'{arousal_rating}%', horizontalalignment='center', verticalalignment='center', color='black', fontsize=12)

#Labels
label_positions = [(positions[i] + positions[i + 1]) / 2 for i in range(len(sections))]
ax.set_yticks([])
ax.set_xlim(0, 100)
ax.set_xticks(label_positions)
ax.set_xticklabels(sections)


for spine in ax.spines.values():
    spine.set_visible(False)

plt.title('Arousal Rating',y=-0.4)
plt.show()
    



