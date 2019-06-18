import nltk.classify.util
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from nltk.stem import PorterStemmer
import csv
from nltk.util import ngrams
from nltk.classify import NaiveBayesClassifier


doc_set = list()
def read_file():
    with open('./Document/SMSSpamCollection', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='excel', delimiter='\t')
        for row in reader:
            doc_set.append(row)
        #print(doc_set)
        #print(len(doc_set))
    csvFile.close()

def preprocessing():
    for data in doc_set:
        stopWords = set(stopwords.words('english'))
        words = word_tokenize(data[1])
        #print("word tokenized: " , words)
        wordsFiltered = []
        for w in words:
            if w not in stopWords:
                wordsFiltered.append(w)
        #print("delete stop words: ",wordsFiltered)
        ps = PorterStemmer()
        for i in range(len(wordsFiltered)):
            wordsFiltered[i] = ps.stem(wordsFiltered[i])
            #print("stem word: ",word)
        data[1] = wordsFiltered

def create_ngram_features(words, n=2):
    ngram_vocab = ngrams(words, n)
    my_dict = dict([(ng, True) for ng in ngram_vocab])
    return my_dict

#for fileid in movie_reviews.fileids('pos'):
#    print(movie_reviews.words(fileid))
read_file()
preprocessing()
print(doc_set)


for n in [2]:
    pos_data = []
    for line in doc_set:
        if (line[0] == "ham"):
            words = line[1]
            pos_data.append((create_ngram_features(words, n), "positive"))

    neg_data = []
    for line in doc_set:
        if (line[0] == "spam"):
            words = line[1]
            neg_data.append((create_ngram_features(words, n), "negative"))
