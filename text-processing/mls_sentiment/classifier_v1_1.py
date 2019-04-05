import nltk
import pickle
import classifier_v1 as v1

classifier
pickle_in = open("naivebayes.pickle","rb")
classifier = pickle.load(pickle_in)
pickle_in.close()

def predict_sentiment(p_string):
    return classifier.classify(v1.extract_features(p_string.split()))

v_value = predict_sentiment("I am happy")
print(v_value)