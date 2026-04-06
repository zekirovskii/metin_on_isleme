"""
Amaç: Temel veri temizleme işlemlerini gerçekleştirmek.
      - fazla boşlukları kaldırma
      - büyük harfleri küçük harfe çevirme
      - noktalama işaretlerini kaldırma
      - özel karakterleri kaldırma
      - yazım hatalarını düzeltme
      - html etiketlerini kaldırma

pip install textblob beautifulsoup4
"""

# fazla boşlukları kaldırma
raw_text= "Python,    Google       NLP    dersi"
print(raw_text.split())
normalized_text = " ".join(raw_text.split())
print("fazla boşlukları kaldırma: ", normalized_text)

# büyük harfleri küçük harfe çevirme
raw_text = "PYTHON, GooGLE NLP DERSİ"
normalized_text_2 = raw_text.lower()
print(f"büyük harfleri küçük harfe çevirme: {normalized_text_2}")

# noktalama işaretlerini kaldırma
import string
raw_text = "AI Naturallanguageprocessing, Python! Dersi."
normalized_text_3 = raw_text.translate(str.maketrans("", "", string.punctuation)) # noş string ile değiştirir
print(f"noktalama işaretlerini kaldırma: {normalized_text_3}")

# özel karakterleri kaldırma %, $, &, @, # gibi
import re # regular expression (düzenli ifadeler)
raw_text = "Naturel @ Language #Processing, Python! Dersi."
normalized_text_4 = re.sub(r"[^a-zA-Z0-9\s]", "", raw_text) # a-zA-Z0-9 ve boşluk haricindeki karakterleri

print(f"özel karakterleri kaldırma: {normalized_text_4}")

# yazım hatalarını düzeltme
from textblob import TextBlob
raw_text = "It is amazig in 2025"
normalized_text_5 = TextBlob(raw_text).correct()
print(f"yazım hatalarını düzeltme: {normalized_text_5}")

# html etiketlerini kaldırma
from bs4 import BeautifulSoup
raw_text = "<html><body><h1>Python NLP Dersi</h1>"
normalized_text_6 = BeautifulSoup(raw_text, "html.parser").get_text()
print(f"html etiketlerini kaldırma: {normalized_text_6}")