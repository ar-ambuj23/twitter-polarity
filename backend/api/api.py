import json
import tweepy

credentials_file = 'credentials/twitter_credentials.json'

with open(credentials_file) as json_file:
    credentials = json.load(json_file)

auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth, tweet_mode='extended')    

def searchByHashtag(hashtag, count, lang='en', geocode=None, result_type='mixed'):
    tweets = api.search('#{}'.format(hashtag), count=count, lang=lang, geocode=geocode, result_type=result_type, tweet_mode='extended')
    return [(tweet.full_text, tweet.created_at) for tweet in tweets]