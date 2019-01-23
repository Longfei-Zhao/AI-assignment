import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data import read_as_df
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from itertools import chain
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support

_pathToDataset = '../data/assign_data_train/'
stemmer = SnowballStemmer("english")

def loadingDataset():
    '''
        Dataset loading
    '''
    return read_as_df(_pathToDataset)

def preprocessor(text):
    '''
        turns text into tokens after tokenization, stemming, stop words removal
        imput:
            - text: document to process
        output: =>
            - tokens: list of tokens after tokenization, stemming, stop words removal
    '''

    #Tokenization
    __tokenization_pattern = r'''(?x)          # set flag to allow verbose regexps
            \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
          | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
          | \w+(?:-\w+)*        # words with optional internal hyphens
          | \.\.\.              # ellipsis
          | [][.,;"'?():_`-]    #
        '''
    tokenizer = nltk.tokenize.regexp.RegexpTokenizer(__tokenization_pattern)
    tokens = tokenizer.tokenize(text.lower())
    alphabet_tokens = [token for token in tokens if token.isalpha()]

    #Stopwords removal
    en_stopwords = set(stopwords.words('english'))
    non_stopwords = [word for word in alphabet_tokens if not word in en_stopwords]
    #print("number of tokens : {}".format(len(set(non_stopwords))))
    #print("tokens: {}".format(non_stopwords))

    #Stemming
    stems = [str(stemmer.stem(word)) for word in non_stopwords]
    return stems

def analyzeStatistics(dataset):
    fdist = nltk.FreqDist(chain(*dataset['tokens']))
    print(fdist.most_common(10))
    plt.figure(figsize=(15, 6))
    fdist.plot(50,cumulative=False)

def predicate(doc):
    return stemmer.stem('research') in doc or stemmer.stem('seminar') in doc

if __name__ == "__main__":

    dataset = loadingDataset()
    dataset['tokens'] = dataset['text'].apply(preprocessor)
    dataset['features'] = dataset['tokens'].apply(set)
    #matches = dataset['features'].apply(predicate)
    print(dataset)
    bow_vectorizer = CountVectorizer(lowercase = False,
                                     tokenizer = lambda x: x, # because we already have tokens available
                                     stop_words = None, ## stop words removal already done from NLTK
                                     max_features = 5000, ## pick top 5K words by frequency
                                     ngram_range = (1, 1), ## we want unigrams now
                                     binary = False) ## we want as binary/boolean features
    text_vec = bow_vectorizer.fit_transform(dataset.tokens)

    msk = np.random.rand(len(dataset)) < 0.75
    le = LabelEncoder()

    train_X = text_vec[msk]
    test_X = text_vec[~msk]

    y = le.fit_transform(dataset.category)
    train_y = y[msk]
    test_y = y[~msk]
    classifier =  MultinomialNB()
    classifier.fit(train_X, train_y)
    preds_bow = classifier.predict(test_X)
    to_print = [le.inverse_transform(pred) for pred in preds_bow ]
    #print(to_print[:100])
    confusion = confusion_matrix(test_y, preds_bow)
    acc_bow = accuracy_score(test_y, preds_bow)
    precisions_bow, recalls_bow, f1_scores_bow, _ = precision_recall_fscore_support(test_y, preds_bow)

    print("accuracy = {}".format(acc_bow))

    print("{:>25} {:>4} {:>4} {:>4}".format("", "prec", "rec", "F1"))
    for (idx, scores) in enumerate(zip(precisions_bow, recalls_bow, f1_scores_bow)):
        print("{:>25} {:.2f} {:.2f} {:.2f}".format(
            le.inverse_transform(idx), scores[0], scores[1], scores[2]
        ))

    print('confusion matrix:\n{}'.format( confusion) )
    fdist = nltk.FreqDist(chain(*dataset['tokens']))
    print(fdist.most_common(10))

    plt.figure(figsize=(15, 6))  # the size you want
    fdist.plot(50,cumulative=False)
