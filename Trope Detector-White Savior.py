#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


whiteSavior = ['blindsidethe.txt', 'Finding Forrester.txt', 'helpthe.txt', 'Hidden Figures.txt', 'lincoln.txt', 'Million Dollar Arm.txt', 'Radio.txt', 'Remember the Titans.txt', 'The Soloist.txt', 'The Green Book.txt', 'Remember the Titans.txt']
notWhiteSavior = ['500daysofsummer.txt', 'amadeus.txt', 'kingsspeechthe.txt', 'knockedup.txt', 'marypoppins.txt', 'minorityreport.txt', 'perksofbeingawallflowerthe.txt', 'silenceofthelambs.txt', 'terminator.txt', 'titanic.txt']


# In[3]:


fileList = []

for f in whiteSavior:
    file = open(f, 'rt')
    text = file.read()
    fileList.append(text)
    file.close()
fileList


# In[4]:


ws = pd.DataFrame(fileList,columns=['Movie'])
ws


# In[5]:


ws['White Savior'] = 1
ws


# In[6]:


fileList2 = []

for f in notWhiteSavior:
    file = open(f, 'rt')
    text = file.read()
    fileList2.append(text)
    file.close()
fileList

nws = pd.DataFrame(fileList2,columns=['Movie'])
nws['White Savior'] = 0
nws


# In[7]:


df = pd.concat([ws,nws])
df


# In[8]:


from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas, numpy, textblob, string


# In[9]:


train_x, valid_x, train_y, valid_y = model_selection.train_test_split(df['Movie'], df['White Savior'])


# In[10]:


# create a count vectorizer object 
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(df['Movie'])

# transform the training and validation data using count vectorizer object
xtrain_count =  count_vect.transform(train_x)
xvalid_count =  count_vect.transform(valid_x)


# In[11]:


# word level tf-idf
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)
tfidf_vect.fit(df['Movie'])
xtrain_tfidf =  tfidf_vect.transform(train_x)
xvalid_tfidf =  tfidf_vect.transform(valid_x)


# In[20]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
#create a new random forest classifier
rf = RandomForestClassifier()
#create a dictionary of all values we want to test for n_estimators
params_rf = {"n_estimators": [50, 100, 200]}
#use gridsearch to test all values for n_estimators
rf_gs = GridSearchCV(rf, params_rf, cv=5)
#fit model to training data
rf_gs.fit(xtrain_tfidf, train_y)


# In[21]:


#save best model
rf_best = rf_gs.best_estimator_
#check best n_estimators value
print(rf_gs.best_params_)
rfPredictions = rf_gs.predict(xvalid_tfidf)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(valid_y, rfPredictions))


# In[22]:


# Determine the model performance metrics
from sklearn.metrics import classification_report
print(classification_report(valid_y,rfPredictions))


# In[25]:


file = open('avatar.txt', 'rt')
text = file.read()
fileList.append(text)
file.close()

text_tfidf =  tfidf_vect.transform(text)


# In[ ]:




