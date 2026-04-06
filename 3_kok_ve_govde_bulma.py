"""
kök ve gövde bulma (stemming ve lemmatization)
    - stemming: kelimelerin köklerini bulma işlemi. Kökler genellikle gerçek kelime olmayabilir.
      porter stemmer
    - lemmatization: kelimelerin gövdelerini bulma işlemi.
      word net lemmatizer
pip install nltk
"""

import nltk 
nltk.download("wordnet") # lemmatization için gerekli olan veriyi indirir
nltk.download("omw-1.4") # wordnet için ek dil desteği

#stemming
from nltk.stem import PorterStemmer # ingilizce için porter stemmer
stemmer = PorterStemmer() # porter stemmer nesnesi oluşturma
words_stem=["play", "playing", "played", "plays","happily", "happiness","study", "studying", "studies"]

stems= [stemmer.stem(word) for word in words_stem]
print(f"original: {words_stem}")
print(f"stemmed: {stems}")

#lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer() # lemmatizer nesnesi oluşturma
words_lemma = ["running", "ran","gone","better","children","studies"]
lemmas = [lemmatizer.lemmatize(word) for word in words_lemma]
print(f"original: {words_lemma}")
print(f"lemmatized: {lemmas}")