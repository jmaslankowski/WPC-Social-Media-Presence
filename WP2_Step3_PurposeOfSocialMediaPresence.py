# WP2 Social Media Use Case - Classification of Social Media Presence
# If you need more information:
# Contact: j.maslankowski@stat.gov.pl

import pandas as pd
import numpy as np 
import re, nltk
from sklearn.feature_extraction.text import CountVectorizer        
from nltk.stem.porter import PorterStemmer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from collections import Counter

# only ENGLISH STOP WORDS are present in NLTK
# all others must be added like this
POLISH_STOP_WORDS=["ach","aj","albo","bardzo","bez","bo","być","ci","cię","ciebie","co","czy","daleko","dla",
    "dlaczego","dlatego","do","dobrze","dokąd","dość","dużo","dwa","dwaj","dwie","dwoje","dziś",
    "dzisiaj","gdyby","gdzie","go","ich","ile","im","inny","ja","ją","jak","jakby","jaki","je",
    "jeden","jedna","jedno","jego","jej","jemu","jeśli","jest","jestem","jeżeli","już","każdy",
    "kiedy","kierunku","kto","ku","lub","ma","mają","mam","mi","mną","mnie","moi","mój","moja",
    "moje","może","mu","my","na","nam","nami","nas","nasi","nasz","nasza","nasze","natychmiast",
    "nią","nic","nich","nie","niego","niej","niemu","nigdy","nim","nimi","niż","obok","od","około",
    "on","ona","one","oni","ono","owszem","po","pod","ponieważ","przed","przedtem","są","sam","sama",
    "się","skąd","tak","taki","tam","ten","to","tobą","tobie","tu","tutaj","twoi","twój","twoja",
    "twoje","ty","wam","wami","was","wasi","wasz","wasza","wasze","we","więc","wszystko","wtedy",
    "wy","żaden","zawsze","że","z","i","w","a","o","się","za","ale","tym","czym","tego","czego",
    "tylko","będą","będzie","taka","było","te"]


# !!! CHANGE THE FILENAME TO THE ENTERPRISE COLLECTED IN STEP2
test_data_file_name='WP2_test_ENTERPRISE_NAME.csv'
train_data_file_name='WP2_train.csv'
test_data_df = pd.read_csv(test_data_file_name, header=None, delimiter=";")
test_data_df.columns = ["Text"]
train_data_df = pd.read_csv(train_data_file_name, header=None, delimiter=";")
train_data_df.columns = ["Type","TypeText","Text"]
TypeText=['others',  'recruitment',  'marketing',  'enterprise image',  'commercials']

np.mean([len(s.split(" ")) for s in train_data_df.Text])

stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    # !!! replace the line below with your stopwords list like this
    # stop_words=POLISH_STOP_WORDS,
    stop_words = 'english',
    max_features = 85
)

corpus_data_features = vectorizer.fit_transform(
    train_data_df.Text.tolist() + test_data_df.Text.tolist())
corpus_data_features_nd = corpus_data_features.toarray()
corpus_data_features_nd.shape
vocab = vectorizer.get_feature_names()
dist = np.sum(corpus_data_features_nd, axis=0)
X_train, X_test, y_train, y_test  = train_test_split(
        corpus_data_features_nd[0:len(train_data_df)], 
        train_data_df.Type,
        train_size=0.85, 
        random_state=1234)
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)
y_pred = log_model.predict(X_test)

print("Testing the training dataset accuracy...")
print(classification_report(y_test, y_pred))

log_model = LogisticRegression()
log_model = log_model.fit(X=corpus_data_features_nd[0:len(train_data_df)], y=train_data_df.Type)
    
test_pred = log_model.predict(corpus_data_features_nd[len(train_data_df):])
    
import random
spl = random.sample(range(len(test_pred)), len(test_pred))
purpose=[]
for text, type in zip(test_data_df.Text[spl], test_pred[spl]):
    print (TypeText[type-1],':', text)
    purpose.append(TypeText[type-1])

print("The enterprise has the following purpose of the presence in social media:\n" )
c = Counter(purpose)
for letter in c:
    print ('%s: %d' % (letter, c[letter]))