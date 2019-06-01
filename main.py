from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

doc_set = list()
def read_common_words():
    f = open("./Document/SMSSpamCollection", "r")
    for x in f:
        if(x[0:4] == "spam"):
            print((x[5:]))
        elif(x[0:3] == "ham"):
            print((x[4:]))
        doc_set.append(x.lower().rstrip('\n'))
    print(doc_set)
    print(len(doc_set))
    f.close()

def preprocessing():
    data = "ham spam All work and no playing makes jack dull boy. All work and no play makes jack a dull boy."
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(data)
    print(words)
    wordsFiltered = []
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    print(wordsFiltered)
    ps = PorterStemmer()
    for word in wordsFiltered:
        stem_word = ps.stem(word)
        print(stem_word)

read_common_words()