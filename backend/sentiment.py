from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from api import api
from collections import defaultdict, Counter
from scipy.stats import chisquare

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

def polarityByCount(hashtag, count, loc):

    twitter_api = api.TwitterAPI('api/credentials/twitter_credentials.json')
    
    # Get tweets_dict of top n tweets by country for this hashtag 
    tweetsByCount = twitter_api.getTweetsByCount(query=hashtag, count=count, loc=loc)
    list_of_tweets = twitter_api.getFeatures(tweetsByCount, feature_list=['id', 'created_at', 'full_text'])
    print(list_of_tweets)
    
    # Add Sentiment score for each tweet_feature
    for tweet_dict in list_of_tweets:
        tweet_dict['sentiment'] = get_sentiment(tweet_dict['full_text'])
    
    # Get polarity per day for the hashtag
    cols = list(list_of_tweets[0].keys())
    features = [list(tweet_dict.values()) for tweet_dict in list_of_tweets]
    
    tweet_df = pd.DataFrame(columns=cols, data=features)
    tweet_df['sentiment_label'] = tweet_df.sentiment.apply(lambda x: sentiment_label(x))
    date_groups = tweet_df.groupby(by=pd.to_datetime(pd.to_datetime(tweet_df['created_at']).dt.date))
    date_polarity_counts = []
    for date, df in date_groups:
        polarity = dict()
        polarity['date'] = date
        sentiment_counts = df.groupby(by='sentiment_label').count()['id'].to_dict()
        polarity.update(sentiment_counts)
        date_polarity_counts.append(polarity)
    
    return date_polarity_counts


def polarityByDay(hashtag, count, loc):

    twitter_api = api.TwitterAPI('api/credentials/twitter_credentials.json')
    
    # Get n tweets per day for last 7 days
    tweets7DaysByCount = twitter_api.getTweets7DaysByCount(query=hashtag, count=count, loc=loc)
    
    # Get sentiment and sentiment_label for each tweet for each day
    for date in tweets7DaysByCount:
        for tweet_dict in tweets7DaysByCount[date]:
            tweet_dict['sentiment'] = get_sentiment(tweet_dict['full_text'])
            tweet_dict['sentiment_label'] = sentiment_label(tweet_dict['sentiment'])
            
    # Get date_polarity_counts
    date_polarity_counts = []
    labels = [-1, 0, 1]
    for date in tweets7DaysByCount:
        polarity = dict()
        polarity['date'] = date
        sentiment_labels = [d['sentiment_label'] for d in tweets7DaysByCount[date]]
        label_counts = dict(Counter(sentiment_labels))
        for l in labels:
            label_counts[l] = label_counts.get(l, 0)
        try:
            polarity_index = 1. / chisquare(list(label_counts.values()))[0]
        except ZeroDivisionError:
            polarity_index = 0
        polarity['polarity_index'] = polarity_index
        total_tweets = sum(label_counts.values())
        for l in label_counts.keys():
            label_counts[l] /= total_tweets
        polarity.update(label_counts)
        date_polarity_counts.append(polarity)
    
    return date_polarity_counts

def trendingHashtags(woeid, loc, n_results=10, n_tweets=10):
    twitter_api = api.TwitterAPI('api/credentials/twitter_credentials.json')
    trend_info = twitter_api.getTrendsByWOEID(woeid)

    landing_page = []
    for trend in trend_info['trends'][:n_results]:
        hashtag_info = {}
        query = trend['query']
        date_counts = polarityByDay(hashtag=query, loc=loc, count=n_tweets)
        hashtag_info['date_polarity_counts'] = date_counts
        hashtag_info.update(trend)
        landing_page.append(hashtag_info)
    
    return landing_page