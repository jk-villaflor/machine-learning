import settings
import helpers
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

v_playerNames = []

#   fetch data from database
v_conn = helpers.open_dbcon(settings.MONGO_URI)
v_players = helpers.get_players(settings.MONGO_DATABASE, settings.MDB_players, v_conn)

#sanitize player_name
v_playerNames = helpers.get_player_query(v_players, settings.MDB_player_name_col)

#   perform sentiment analysis and quantify player tweets
helpers.get_player_vSentiments(v_playerNames, settings.MONGO_DATABASE, settings.MDB_tweets, v_conn, settings.MDB_tweets_coltext)


#   save results into database



helpers.close_dbcon(v_conn)

#v_string = 'hi gorgeous'
#analyzer = SentimentIntensityAnalyzer()
#vs = analyzer.polarity_scores(v_string)
#print(vs)

#tb = TextBlob(v_string)
#print(vs)
#print(tb.sentiment)