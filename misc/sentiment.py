import tweepy
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import glob
import json
import os

# Copy Credentials folder
credentials_path = 'Credentials/twitter_credentials.json'
with open(credentials_path, "r") as file:
    cred = json.load(file)
    consumer = cred["CONSUMER_KEY"]
    consumer_secret = cred["CONSUMER_SECRET"]
    access = cred["ACCESS_KEY"]
    access_secret = cred["ACCESS_SECRET"]

def init_api():
    auth = tweepy.OAuthHandler(consumer_key=consumer, consumer_secret=consumer_secret)
    auth.set_access_token(key=access, secret=access_secret)
    api = tweepy.API(auth)
    return api

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

if __name__ == "__main__":
    # Driver
    api = init_api()
    hashtag = input("Enter a hashtag: ")
    loc = 'USA'
    places = api.geo_search(query="USA", granularity="country")
    query = '{} place:{}'.format(hashtag, places[0].id)
    tweets = api.search(q=query, count=300, result_type='mixed', language='en')
    features = []
    for tweet in tweets:
        tweet_text = tweet.text
        sentiment_score = get_sentiment(tweet_text)
        content = [tweet.id, tweet.created_at, tweet.user.verified, tweet.text, sentiment_score]
        features.append(content)
        print(tweet_text)
        print(sentiment_score)
    cols = ['id', 'timestamp', 'verified', 'text', 'sentiment']
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
    
