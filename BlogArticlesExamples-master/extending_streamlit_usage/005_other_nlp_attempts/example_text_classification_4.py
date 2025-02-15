#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
[path]
cd /Users/brunoflaven/Documents/01_work/blog_articles/extending_streamlit_usage/005_other_nlp_attempts/

[file]
python example_text_classification_4.py

"""
## SOURCE :: https://towardsdatascience.com/text-analysis-feature-engineering-with-nlp-502d6ea9225d
## SOURCE :: https://www.experfy.com/blog/ai-ml/text-classification-with-nlp-tf-idf-vs-word2vec-vs-bert/


## for data
import pandas as pd
import collections
import json
## for plotting
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud
## for text processing
import re
import nltk
## for language detection
import langdetect
## for sentiment
from textblob import TextBlob
## for ner
import spacy
## for vectorizer
from sklearn import feature_extraction, manifold
## for word embedding
import gensim.downloader as gensim_api
## for topic modeling
import gensim


lst_dics = []
# Change to bigger json News_Category_Dataset_v2.json if needed
with open('datas/News_Category_Dataset_v2_light.json', mode='r', errors='ignore') as json_file:
    for dic in json_file:
        lst_dics.append(json.loads(dic))


## print the first one
print("\n--- OUTPUT_1")
print(lst_dics[0])



## create dtf
dtf = pd.DataFrame(lst_dics)
## filter categories
dtf = dtf[dtf["category"].isin(['ENTERTAINMENT', 'POLITICS', 'TECH'])][[
    "category", "headline"]]
## rename columns
dtf = dtf.rename(columns={"category": "y", "headline": "text"})
## print 5 random rows
print("\n--- OUTPUT_2")
print (dtf.sample(5))

# SHOW IMAGE
# define axis
# x = "y"
# fig, ax = plt.subplots()
# fig.suptitle(x, fontsize=12)
# dtf[x].reset_index().groupby(x).count().sort_values(by= "index").plot(kind="barh", legend=False, ax=ax).grid(axis='x')
# plt.show()


# Language Detection
txt = dtf["text"].iloc[0]
print("\n--- OUTPUT_3")
print(txt, " --> ", langdetect.detect(txt))


# Add a column with the language information for the whole dataset

dtf['lang'] = dtf["text"].apply(
    lambda x: langdetect.detect(x)if x.strip() != "" else "")

# print head dataset
# CAUTION VERY LONG PROCESS, BE PATIENT
# show the dataset with the language column
# dtf.head()

# show repartition by lang in a graphic
# CAUTION VERY LONG PROCESS, BE PATIENT
# x = "lang"
# fig, ax = plt.subplots()
# fig.suptitle(x, fontsize=12)
# dtf[x].reset_index().groupby(x).count().sort_values(by="index").plot(kind="barh", legend=False, ax=ax).grid(axis='x')
# plt.show()

print("\n--- OUTPUT_4")
# Text Preprocessing
# CAUTION VERY LONG PROCESS, BE PATIENT
print("--- original ---")
print(txt)

print("--- cleaning ---")
txt = re.sub(r'[^\w\s]', '', str(txt).lower().strip())
print(txt)

print("--- tokenization ---")
txt = txt.split()
print(txt)


# Load generic stop words for the English vocabulary with NLTK
lst_stopwords = nltk.corpus.stopwords.words("english")
print("\n--- OUTPUT_5")
print(lst_stopwords)

# remove those stop words from the first news headline

print("\n--- OUTPUT_6")
print("--- remove stopwords ---")
txt = [word for word in txt if word not in lst_stopwords]
print(txt)

print("\n--- OUTPUT_7")
# Stemming and Lemmatization
print("--- stemming ---")
ps = nltk.stem.porter.PorterStemmer()
print([ps.stem(word) for word in txt])

print("--- lemmatisation ---")
lem = nltk.stem.wordnet.WordNetLemmatizer()
print([lem.lemmatize(word) for word in txt])


'''
Preprocess a string.
:parameter
    :param text: string - name of column containing text
    :param lst_stopwords: list - list of stopwords to remove
    :param flg_stemm: bool - whether stemming is to be applied
    :param flg_lemm: bool - whether lemmitisation is to be applied
:return
    cleaned text
'''


def utils_preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):
    ## clean (convert to lowercase and remove punctuations and characters and then strip)
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())

    ## Tokenize (convert from string to list)
    lst_text = text.split()
    ## remove Stopwords
    if lst_stopwords is not None:
        lst_text = [word for word in lst_text if word not in
                    lst_stopwords]

    ## Stemming (remove -ing, -ly, ...)
    if flg_stemm == True:
        ps = nltk.stem.porter.PorterStemmer()
        lst_text = [ps.stem(word) for word in lst_text]

    ## Lemmatisation (convert the word into root word)
    if flg_lemm == True:
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        lst_text = [lem.lemmatize(word) for word in lst_text]

    ## back to string from list
    text = " ".join(lst_text)
    return text


# be sure to define dtf, don't mess with the arguments
dtf["text_clean"] = dtf["text"].apply(lambda x:utils_preprocess_text(x, flg_stemm=False, flg_lemm=True, lst_stopwords=lst_stopwords))

print("\n--- OUTPUT_8")
# output
print(dtf.head())

print("\n--- OUTPUT_9")
# Print the first line original and then the same but cleaned
print(dtf["text"].iloc[0], " --> ", dtf["text_clean"].iloc[0])


# Length Analysis


"""
- word count: counts the number of tokens in the text (separated by a space)

- character count: sum the number of characters of each token

- sentence count: count the number of sentences (separated by a period)

- average word length: sum of words length divided by the number of words (character count/word count)

- average sentence length: sum of sentences length divided by the number of sentences (word count/sentence count)

"""
# word_count
dtf['word_count'] = dtf["text"].apply(lambda x: len(str(x).split(" ")))

# char_count
dtf['char_count'] = dtf["text"].apply(
    lambda x: sum(len(word) for word in str(x).split(" ")))

# sentence_count
dtf['sentence_count'] = dtf["text"].apply(lambda x: len(str(x).split(".")))

# avg_word_length
dtf['avg_word_length'] = dtf['char_count'] / dtf['word_count']

# avg_sentence_lenght
dtf['avg_sentence_lenght'] = dtf['word_count'] / dtf['sentence_count']

print("\n--- OUTPUT_10")
# output
dtf.head()


"""
What’s the distribution of those new variables with respect to the target? To answer that I’ll look at the bivariate distributions (how two variables move together). First, I shall split the whole set of observations into 3 samples (Politics, Entertainment, Tech), then compare the histograms and densities of the samples. If the distributions are different then the variable is predictive because the 3 groups have different patterns.
For instance, let’s see if the character count is correlated with the target variable.

"""

# x, y = "char_count", "y"
# fig, ax = plt.subplots(nrows=1, ncols=2)
# fig.suptitle(x, fontsize=12)
# for i in dtf[y].unique():
#     sns.distplot(dtf[dtf[y] == i][x], hist=True, kde=False,
#                  bins=10, hist_kws={"alpha": 0.8},
#                  axlabel="histogram", ax=ax[0])
#     sns.distplot(dtf[dtf[y] == i][x], hist=False, kde=True,
#                  kde_kws={"shade": True}, axlabel="density",
#                  ax=ax[1])
# ax[0].grid(True)
# ax[0].legend(dtf[y].unique())
# ax[1].grid(True)
# plt.show()


# Sentiment Analysis
dtf["sentiment"] = dtf["text"].apply(lambda x:TextBlob(x).sentiment.polarity)


print("\n--- OUTPUT_11")
# output
print(dtf.head())

print("\n--- OUTPUT_12")
# output the sentiment for the first sentence
# print(dtf["text"].iloc[0], " --> ", dtf["sentiment"].iloc[0])


# USING SPACY

# Named-Entity Recognition

## call model
#ner = spacy.load("en_core_web_lg")
## tag text
# txt = dtf["text"].iloc[0]
# doc = ner(txt)
## display result
# spacy.displacy.render(doc, style="ent")


# CAUTION VERY LONG PROCESS, BE PATIENT
## tag text and exctract tags into a list
# dtf["tags"] = dtf["text"].apply(lambda x: [(tag.text, tag.label_) for tag in ner(x).ents])
## utils function to count the element of a list


def utils_lst_count(lst):
    dic_counter = collections.Counter()
    for x in lst:
        dic_counter[x] += 1
    dic_counter = collections.OrderedDict(
        sorted(dic_counter.items(),
               key=lambda x: x[1], reverse=True))
    lst_count = [{key: value} for key, value in dic_counter.items()]
    return lst_count


## count tags
dtf["tags"] = dtf["tags"].apply(lambda x: utils_lst_count(x))

## utils function create new column for each tag category


def utils_ner_features(lst_dics_tuples, tag):
    if len(lst_dics_tuples) > 0:
        tag_type = []
        for dic_tuples in lst_dics_tuples:
            for tuple in dic_tuples:
                type, n = tuple[1], dic_tuples[tuple]
                tag_type = tag_type + [type]*n
                dic_counter = collections.Counter()
                for x in tag_type:
                    dic_counter[x] += 1
        return dic_counter[tag]
    else:
        return 0


## extract features
tags_set = []
for lst in dtf["tags"].tolist():
    for dic in lst:
        for k in dic.keys():
            tags_set.append(k[1])
tags_set = list(set(tags_set))
for feature in tags_set:
    dtf["tags_"+feature] = dtf["tags"].apply(lambda x:utils_ner_features(x, feature))

## print result
print("\n--- OUTPUT_13")
print(dtf.head())

# output image
# Unpack the column “tags” we created in the previous code.
# not working
"""
y = "ENTERTAINMENT"
 
tags_list = dtf[dtf["y"]==y]["tags"].sum()
map_lst = list(map(lambda x: list(x.keys())[0], tags_list))
dtf_tags = pd.DataFrame(map_lst, columns=['tag','type'])
dtf_tags["count"] = 1
dtf_tags = dtf_tags.groupby(['type',  
                'tag']).count().reset_index().sort_values("count", 
                 ascending=False)
fig, ax = plt.subplots()
fig.suptitle("Top frequent tags", fontsize=12)

# change
# sns.barplot(x="count", y="tag", hue="type", data=dtf_tags.iloc[:top,:], dodge=False, ax=ax)
# sns.barplot(x="count", y="tag", hue="type", data=dtf_tags.iloc[:,:], dodge=False, ax=ax)

# sns.barplot(x="count", y="tag", hue="type", data=dtf_tags.iloc[[0,2], [0,1]], dodge=False, ax=ax)

# exemples
# df.iloc[[0,2], [0,1]]
# print(df.iloc[:,0:4])
sns.barplot(x="count", y="tag", hue="type", data=dtf_tags.iloc[:,0:4], dodge=False, ax=ax)

ax.grid(axis="x")
plt.show()
"""


## predict wit NER
txt = dtf["text"].iloc[0]
entities = ner(txt).ents
## tag text
tagged_txt = txt
for tag in entities:
    tagged_txt = re.sub(tag.text, "_".join(tag.text.split()),
                        tagged_txt)
## show result
print("\n--- OUTPUT_14")
print(tagged_txt)





