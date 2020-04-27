#import libs
import pandas as pd
import re
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

#read the data
# delimitor parameter specifies the type of delimiter and qutoing parameter is used to ignore quotes inside the dataset
# - when the code number is 3
dataset = pd.read_csv("Restaurant_Reviews.tsv" , delimiter='\t' , quoting= 3)

#our corpus data
corpus = []
for i in range(len(dataset)):
    # clean the dataset
    review = dataset['Review'][i]
    review = re.sub('[^a-zA-Z]', ' ', review)  # include only letters from a - z and A - Z
    review = review.lower().split()  # change to lower case and change the string into a list of words
    ps = PorterStemmer()  # stemmer object
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]  # remove useless words from the array and apply stemming
    review = ' '.join(review)  # join the list into the orignal sentense
    corpus.append(review)
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values

X_train , X_test , y_train , y_test = train_test_split(X ,y , test_size=0.25 , random_state=0)

classifier = GaussianNB()
classifier.fit(X_train , y_train)
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test , y_pred)
print(cm)

# accuracy = (67 + 113) / 200 , for testing the accuracy
