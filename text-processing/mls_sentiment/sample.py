import nltk
import pickle

    
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# def countpositive(tweets):
# 	count = 0
# 	for string in tweets:
# 		if classifier.classify(extract_features(string.split()))== "positive":
# 			count = count + 1
# 	return count

# def PlayerScore(tweets):
#     count = 0
#     name = tweets[0][0]
#     for tweet in tweets:
#             if classifier.classify(extract_features(tweet[1].split()))== "positive":
#                 count = count + 1
#     print(name, ": " , count)
    
def get_data(p_location):
    data=[]
    with open(p_location,'rb') as my_file:
        data = my_file.readlines()
    return data



training_data = []
tweets = []
test_tweets = [("I feel happy this morning."),
("Larry is my friend."),
("I do not like that man."),
("My house is not great."),
("Your song is annoying."),
("My enemy is amazing.")]

# training_set = nltk.classify.apply_features(extract_features, tweets)
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# classifier.show_most_informative_features(15)

# save the classifier
# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
