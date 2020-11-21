import json
import tweepy
import os
import datetime
from collections import defaultdict

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
    
    def getTweets7DaysByCount(self, query, count, loc=None, lang='en', result_type='mixed'):

        listOfDates = self.getListOfLast7Dates(datetime.date.today())
        
        # If Country(loc) given, search on basis of country
        if(loc):
            placeId = self.getPlaceIdByCountry(loc)
            query = '{} place:{}'.format(query, placeId)
        
        d = defaultdict(list)
        for dateIdx in range(len(listOfDates)-1):
            tweets_cursor = self.getCursor(query=query, dates=(listOfDates[dateIdx], listOfDates[dateIdx+1]), count=count, lang=lang, result_type=result_type)
            for tweet in tweets_cursor:
                d[datetime.datetime.strptime(listOfDates[dateIdx], '%Y-%m-%d')].append({'id':tweet._json['id'], 'full_text':tweet._json['full_text']})

        return d

        
    def getCursor(self, query, dates, count, lang, result_type):
        cursor = tweepy.Cursor(
            self.api.search,
            q = query,
            since = dates[0],
            until = dates[1],
            lang = lang,
            result_type = result_type,
            tweet_mode ='extended')
        return cursor.items(count)
        
        
    def getListOfLast7Dates(self, end_date):
        start_date = end_date - datetime.timedelta(days=6)
        delta = datetime.timedelta(days=1)
        listOfDates = []
        while start_date <= end_date+datetime.timedelta(days=1):
            listOfDates.append(start_date.strftime('%Y-%m-%d'))
            start_date += delta
        return listOfDates
        

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