# -*- coding: utf-8 -*-
"""Stemming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gqlib554fK7khRTJ9UdrC6DbTMmj_jOB
"""

import spacy
nlp = spacy.load('en_core_web_sm')
doc2 = nlp(u"We're here to help! Send snail-mail, email fahad@gmail.com or visit us at http://www.fahadhussaincs.blogspot.com!")
for t in doc2:
    print(t)

doc3 = nlp(u'A 5km NYC cab ride costs $10.30')
for t in doc3:
    print(t)

doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for t in doc4:
    print(t)

# ----   Porter Stemmer   ------

# Import the toolkit and the full Porter Stemmer library
import nltk
from nltk.stem.porter import *

p_stemmer = PorterStemmer()
words = ['run','runner','running','ran','runs','easily','fairly']

for word in words:
    print(word+' --> '+p_stemmer.stem(word))

#SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')

words = ['run','runner','running','ran','runs','easily','fairly']
# words = ['generous','generation','generously','generate']

for word in words:
    print(word+' --> '+s_stemmer.stem(word))

# ----Do Some more practice -----

words = ['consolingly']

print('Porter Stemmer:')
for word in words:
    print(word+' --> '+p_stemmer.stem(word))

print('Porter2 Stemmer:')
for word in words:
    print(word+' --> '+s_stemmer.stem(word))

# Stemming has its drawbacks. If given the token saw, stemming might always return saw, whereas lemmatization would likely return either
# see or saw depending on whether the use of the token was as a verb or a noun. As an example, consider the following:

phrase = 'I am meeting him tomorrow at the meeting'
for word in phrase.split():
    print(word+' --> '+p_stemmer.stem(word))











# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')

var1 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")

for token in var1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)

def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')

var2 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")
show_lemmas(var2)

var3 = nlp(u"I am meeting him tomorrow at the meeting.")
show_lemmas(var3)

var4 = nlp(u"That's of the greate person in the world")
show_lemmas(var4)

