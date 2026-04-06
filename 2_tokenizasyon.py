"""
doğal dil işleme (NLP) için temel adımlardan biri olan tokenizasyon işlemi
    - kelime tokenizasyonu
    - cümle tokenizasyonu

pip install nltk
"""

import nltk # natural language toolkit
nltk.download("punkt") # tokenizasyon için gerekli olan veriyi indirir

# örnek metin
raw_text = "Python, Google NLP dersi. Doğal dil işleme çok eğlenceli! NLP eğitimi ilerleyen aşamalarda LLM konusunu da içerecek."

# kelime tokenizasyonu
word_tokens = nltk.word_tokenize(raw_text)
print("kelime tokenizasyonu: ", word_tokens)

#sentence tokenizasyonu
sentence_tokens = nltk.sent_tokenize(raw_text)
print("cümle tokenizasyonu: ", sentence_tokens)