# -*- coding: utf-8 -*-

import re
import pickle

lemmaDict = {}
stop_words = []

def loadLemmatiser(file):
    file = open(file, encoding="utf8")
    print(file)
    for line in file:
        line=line.strip()
        line_words=' '.join(line.split())
        line_words=line_words.split(' ')
        word= line_words[0]
        lemma=line_words[2].split('.')[0]
        if lemma.strip()!="":
            lemmaDict[word]= lemma

def loadStopwords(file):
    file = open(file, encoding="utf8")
    for line in file:
        stop_words.append(line)
    file.close()


def preprocessing(input_string):
    input_string = input_string.strip()
    input_string = re.sub(r'\d+', '', input_string)
    punc = '''!()-[]{};:'"‘’\,<>./?@#$%^&*_~'''

    input_str = ''
    for i in range(len(input_string)):  
        if input_string[i] in punc:
            if i == 0 or i == len(input_string) - 1:
                continue

            elif input_string[i+1] == ' ' or input_string[i-1] == ' ':
                continue

            else:
                input_str += ' '

        else:
            input_str += input_string[i]

    input_str = input_str.split()
    
    lemmatised_ = []
    
    for i in input_str:
        if i not in stop_words:
            if i in lemmaDict:
                lemmatised_.append(lemmaDict[i])
            else:
                lemmatised_.append(i)

    lemmatised_ =' '.join(lemmatised_)
    
    return lemmatised_


def main(input_text):
    lang_lemma = "project/models/telugu.lemma"
    loadLemmatiser(lang_lemma)


    stop_txt = 'project/models/telugu_stop.txt'
    loadStopwords(stop_txt)

    d = {'Nation':1,'Entertainment':2,'Business':3,'Sports':4,'Editorial':5,'Crime':6}
    di = {}
    for k in d.keys():
        di[d[k]] = k

    clf = pickle.load(open(r'project/save/model','rb')) 
    tfidf = pickle.load(open(r'project/save/tfidf','rb')) 


    input_text = [preprocessing(input_text)]
    test = tfidf.transform(input_text)
    cls = clf.predict(test)[0]
    print(di[cls])
    return di[cls]

