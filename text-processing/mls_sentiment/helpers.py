from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as vaderSent
from textblob import TextBlob

#v_tanalyzer = TextBlob()


def open_dbcon(i_connection_string):
    return MongoClient(i_connection_string)

def close_dbcon(i_conn):
    i_conn.close()
    pass

def get_players(i_dbname, i_collection, i_conn):
    db = i_conn[i_dbname]
    player_collection = db[i_collection]
    return player_collection.find()

def get_player_query(i_players,i_col_name):
    o_playerQuery = []
    for player in i_players:
        if(',' in player[i_col_name]):
            o_playerQuery.append((player[i_col_name].split()[1] + player[i_col_name].split()[0]).strip(','))
        else:
            o_playerQuery.append(player[i_col_name])
    return o_playerQuery

def get_player_tweets(i_dbname, i_collection, i_conn, i_searchPhrase):
    db = i_conn[i_dbname]
    tweets_collection = db[i_collection]
    return  tweets_collection.find(i_searchPhrase)

def get_player_vSentiments(i_playerList, i_dbname, i_collName, i_conn, i_text_col):
    v_vanalyzer = vaderSent() #<- The sith sent me
    v_pos_ctr = 0
    v_neg_ctr = 0

    for player in i_playerList:
        print(player)
        v_player_tweets = get_player_tweets(i_dbname, i_collName, i_conn, {i_text_col :{'$regex':'.*'+player+'.*'}})
        if(v_player_tweets.count() > 0):
            for tweet in v_player_tweets:
                print(v_vanalyzer.polarity_scores(tweet[i_text_col]))
            pass
    pass
