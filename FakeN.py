#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:59:03 2018

@author: prathamesh
"""
threshold=7
from sklearn.datasets import fetch_20newsgroups

#categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

twenty_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42)

print(len(twenty_train.target_names))
print(len(twenty_train.data))
print(twenty_train.target_names)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
#print(twenty_train.data)
X_train_counts=count_vect.fit_transform(twenty_train.data)
#print(X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer=TfidfTransformer()
X_train_tfidf=tfidf_transformer.fit_transform(X_train_counts)

#print(X_train_tfidf.shape)

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(X_train_tfidf,twenty_train.target)

#docs_new=['God is love','OpenGL on the GPU is fast','Student commits suicide']
print('Enter title of the news')
userTitle=input()
docs_new=list(userTitle)

#docs_new=['God is love','OpenGL on the GPU is fast','Student commits suicide']
X_new_counts=count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted=clf.predict_proba(X_new_tfidf)
predicted=predicted*100
predictedn=predicted[0]
print(predictedn)

ans=0  
for i in predicted:
    for j in i:
        if(j>=threshold):
            ans=1
            print('{} is real'.format(userTitle))
        if(ans==1):
            break
    if(ans==1):
        break  
      
if(ans==0):
    print('{} is fake'.format(userTitle))

'''if(True):
    print('{} is real'.format())
else:
    print('{} is fake'.format())'''

'''for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))
    print('{} --> {}  {}'.format(doc,twenty_train.target_names[category],predicted[category]))'''
'''ans=0  
for i in predicted:
    for j in i:
        if(j>=threshold):
            ans=1
            print('{} is real'.fomrat(usertitle))
    
if(ans==0):
    print('{} is fake'.format(usertitle))'''
    
'''from sklearn.pipeline import Pipeline
text_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',MultinomialNB())])
text_clf.fit(twenty_train.data, twenty_train.target)

from sklearn.linear_model import SGDClassifier

import numpy as np
docs_test=['God is love','OpenGL runs fast on GPU']
predicted=text_clf.predict(docs_test)
print(np.mean(predicted==60))

#text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42,max_iter=5, tol=None))])
text_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',SGDClassifier())])'''
