import tweepy
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
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

if __name__ == "__main__":
    # Driver
    api = init_api()
    hashtag = input()
    tweets = api.search(q=hashtag, count=100, result_type='popular', language='en')
    for tweet in tweets:
        tweet_text = tweet.text
        sentiment_score = get_sentiment(tweet_text)
        print(tweet_text)
        print(sentiment_score)
        