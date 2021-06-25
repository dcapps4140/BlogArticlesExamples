#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
[path]
cd /Users/brunoflaven/Documents/01_work/blog_articles/extending_streamlit_usage/001_nlp_spacy_python_realp/


[file]
python 005_nlp_spacy_python.py





# source
Source: https://realpython.com/natural-language-processing-spacy-python/


"""

import spacy

# EN
nlp = spacy.load('en_core_web_sm')
# FR
# nlp = spacy.load('fr_core_news_sm')

print("\n --- result_1")
# EN
print("EN spacy loaded")

# FR
# print("FR spacy loaded")

# STOP WORDS
# EN
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

# FR
# spacy_stopwords = spacy.lang.fr.stop_words.STOP_WORDS

nb_spacy_stopwords = len(spacy_stopwords)
print("\n --- nb_spacy_stopwords")
print(nb_spacy_stopwords)

# for stop_word in list(spacy_stopwords)[:10]:
#      print(stop_word)

# print all stopwords
for stop_word in list(spacy_stopwords):
      print(stop_word)


all_file_text = (
                'Bruno Flaven has been a Project Manager in a wide variety of Internet business applications both in Mobile and in Desktop for 20 years now.'
                
                'You can ﬁnd more information about his professional life on his personal website (www.ﬂaven.fr) or his linkedin proﬁle: https://fr.linkedin.com/in/brunoﬂaven. He is currently working for a Paris-base In France Media Monde (FMM) mostly on mobile applications (iOS and Android). He is currently P.O for a Backoffice project made with Symfony.'
                
                'He also made few trainings to facilitate the handling of the tools that he helps to make.')




# file_name = 'article_bf_1.txt'
# file_name = 'article_bf_2.txt'
# all_file_text = open(file_name).read()

"""
# Stop words like is, a, for, the, and in are not printed in the output
print("\n --- result_2")
all_file_doc = nlp(all_file_text)
for token in all_file_doc:
    if not token.is_stop:
        print(token)
"""

print("\n --- result_3")
# You can also create a list of tokens not containing stop words.
all_file_doc = nlp(all_file_text)
all_file_no_stopword_doc = [
    token for token in all_file_doc if not token.is_stop]
print(all_file_no_stopword_doc)

