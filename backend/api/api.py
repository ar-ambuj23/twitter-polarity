import json
import tweepy
import os

class TwitterAPI():
    def __init__(self, credentials_file_path = os.path.join(os.getcwd(),'credentials/twitter_credentials.json')):
        
        credentials = self.get_credentials(credentials_file_path)
        auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
        auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def get_credentials(self, credentials_file_path):
        with open(credentials_file_path) as json_file:
            credentials = json.load(json_file)
        return credentials

    def searchByHashtag(self, hashtag, count, lang='en', geocode=None, result_type='mixed'):
        tweets = self.api.search('#{}'.format(hashtag), count=count, lang=lang, geocode=geocode, result_type=result_type, tweet_mode='extended')
        return [{'full_text':tweet.full_text, 'created_at':tweet.created_at} for tweet in tweets]