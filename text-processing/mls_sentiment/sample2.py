from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as vaderSent
from textblob import TextBlob


v_vanalyzer = vaderSent()
v_score = v_vanalyzer.polarity_scores("I feel great!")
print("=======Vader Sentiment stats=======")
print(v_score)

v_tanalyzer = TextBlob("I feel great!")
print("=======TextBlob Sentiment Stats=======")
print(v_tanalyzer.sentiment)