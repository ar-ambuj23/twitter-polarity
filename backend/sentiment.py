from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from api import api
from collections import defaultdict

import pandas as pd

def get_sentiment(tweet_text):
    sid = SentimentIntensityAnalyzer()
    # Computing the sentiment
    scores = sid.polarity_scores(tweet_text)
    # Dictionary of sentiment scores. We are interested in scores['compund']
    return scores

def sentiment_label(score):
    if score['compound'] > 0.05:
        return 1
    elif score['compound'] < -0.05:
        return -1
    else:
        return 0
    

def perDayPolarity(hashtag, loc, count=500):

    # Get tweets_dict of top n tweets by country for this hashtag 
    twitter_api = api.TwitterAPI('api/credentials/twitter_credentials.json')
    placeId = twitter_api.getPlaceIdByCountry(loc)
    query = '{} place:{}'.format(hashtag, placeId)
    list_of_tweets = twitter_api.search(query=query, count=count)
    
    # Add Sentiment score for each tweet_feature
    for tweet_dict in list_of_tweets:
        tweet_dict['sentiment'] = get_sentiment(tweet_dict['text'])
        
    # Get polarity per day for a hashtag
    cols = list(list_of_tweets[0].keys())
    features = [list(tweet_dict.values()) for tweet_dict in list_of_tweets]
    
    tweet_df = pd.DataFrame(columns=cols, data=features)
    tweet_df['sentiment_label'] = tweet_df.sentiment.apply(lambda x: sentiment_label(x))
    date_groups = tweet_df.groupby(by=pd.to_datetime(tweet_df['timestamp'].dt.date))
    date_polarity_counts = []
    for date, df in date_groups:
        polarity = dict()
        polarity['date'] = date
        sentiment_counts = df.groupby(by='sentiment_label').count()['id'].to_dict()
        polarity.update(sentiment_counts)
        date_polarity_counts.append(polarity)
    
    return date_polarity_counts


