import json
import tweepy
import os

class TwitterAPI():
    def __init__(self, credentials_file_path = os.path.join(os.getcwd(),'credentials/twitter_credentials.json')):
        
        credentials = self.getCredentials(credentials_file_path)
        auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
        auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def getCredentials(self, credentials_file_path):
        with open(credentials_file_path) as json_file:
            credentials = json.load(json_file)
        return credentials

    def search(self, query, count, lang='en', geocode=None, result_type='mixed'):
        tweets = self.api.search(q=query, count=count, lang=lang, geocode=geocode, result_type=result_type, tweet_mode='extended')
        features = []
        for tweet in tweets:
            content = {'id':tweet.id, 'timestamp':tweet.created_at, 'verified':tweet.user.verified, 'text':tweet.full_text}
            features.append(content)
        return features
    
    def getPlaceIdByCountry(self, loc, granularity="country"):
        places = self.api.geo_search(query=loc, granularity="country")
        return places[0].id