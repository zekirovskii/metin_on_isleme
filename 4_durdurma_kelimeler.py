"""
stop words çıkartma yöntemleri
    - ingilizce stop words çıkarma (nltk)
    - türkçe stop words çıkarma (nltk)
    - manuel stop words çıkarma

pip install nltk
"""

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords") # stop words verisini indirir
stop_words_en = set(stopwords.words("english")) # ingilizce stop words seti

# ingilizce stop words çıkarma
eng_text = "This is just a simple example to show how stop words can be removed from sentences"
eng_tex_list = eng_text.split()
print(eng_tex_list)

filtered_eng_text = [word for word in eng_tex_list if word.lower() not in stop_words_en]
print(f"original: {eng_text}")
print(f"ingilizce stop words çıkarma: {filtered_eng_text}")


#türkçe stop words çıkarma
stop_words_tr = set(stopwords.words("turkish")) # türkçe stop words seti
tr_text="Merhaba, bugün sizler ile birlikte Google Nlp eğitimi gerçekleştiriyoruz. Bu eğitim sizler için çok faydalı olacaktır."
tr_text_list = tr_text.split()

filtered_tr_text = [word for word in tr_text_list if word.lower() not in stop_words_tr]
print(f"original: {tr_text}")
print(f"türkçe stop words çıkarma: {filtered_tr_text}")


# manuel stop words çıkarma
custom_tr_stop_words= ["bu", "için", "ile", "ve", "de", "da", "mi", "ki"]
custom_text= "Bu bir denemedir, bunun için amacımız metinlerde ki bazı kelimeleri çıkartmak." 

custom_text_list = custom_text.split()
filtered_custom_text = [word for word in custom_text_list if word.lower() not in custom_tr_stop_words]
print(f"original: {custom_text}")
print(f"manuel stop words çıkarma: {filtered_custom_text}")
