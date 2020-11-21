import json
import tweepy
import os

class TwitterAPI():
    def __init__(self, credentials_file_path = os.path.join(os.getcwd(),'credentials/twitter_credentials.json')):
        
        credentials = self.getCredentials(credentials_file_path)
        auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
        auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def getCredentials(self, credentials_file_path):
        with open(credentials_file_path) as json_file:
            credentials = json.load(json_file)
        return credentials
    
    def getTweetsByCount(self, query, count, loc=None, lang='en', result_type='mixed'):
        _max_queries = 500  # arbitrarily chosen value
        
        # If Country(loc) given, search on basis of country
        if(loc):
            placeId = self.getPlaceIdByCountry(loc)
            query = '{} place:{}'.format(query, placeId)

        tweets = tweet_batch = self.api.search(q=query, count=count, lang=lang, result_type=result_type, tweet_mode='extended')
        ct = 1
        while len(tweets) < count and ct < _max_queries:
            tweet_batch = self.api.search(q=query, 
                                     count=count - len(tweets),
                                     max_id=tweet_batch.max_id, lang=lang, result_type=result_type, tweet_mode='extended')
            tweets.extend(tweet_batch)
            ct += 1
        return tweets

    def getFeatures(self, tweets, feature_list):
        features = []
        for tweet in tweets:
            content = {}
            for feature in feature_list:
                content[feature] = tweet._json[feature]
            features.append(content)
        return features
    
    def getPlaceIdByCountry(self, loc, granularity="country"):
        places = self.api.geo_search(query=loc, granularity="country")
        return places[0].id