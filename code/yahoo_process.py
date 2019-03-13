import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import string

#remove capitalization, stopwords, and punctuation
def process(text) : 
    #remove punctuation/captizalization
    text = str(text)
    text = text.lower()
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    #remove stopwords
    procList = [word for word in nopunc.split() if word not in stopwords.words('english')]
    return ' '.join(procList)

def cleanAndSave(source, dest) : 
    #load data
    df = pd.read_csv(source, names=['class', 'title', 'content', 'answer'])
    X1, X2, X3, Y = df['title'], df['content'], df['answer'], df['class']
    title, question, answer, clss = [], [], [], []
    
    #process text
    for i in range(0, len(X1)) :  
        title.append(process(X1[i]))
        question.append(process(X2[i]))
        answer.append(process(X3[i]))
        clss.append(Y[i])

    #merge processed text columns into dataframe and save
    df = pd.DataFrame({"title" : title, "question" : question, "answer" : answer, "class" : clss})
    df['text'] = df['title'].map(str) + ' ' + df['question'].map(str) + ' ' + df['answer'].map(str)

    df_save = pd.DataFrame({'text': df['text'], "class" : df['class']})
    df_save.to_csv(dest, index=False)

#cleanAndSave('data/yahoo_train_notnull.csv', 'data/yahoo_train_notnull_clean.csv')
#print('done')
