from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from api import api
from collections import defaultdict

def get_sentiment(tweet_text):
    sid = SentimentIntensityAnalyzer()
    # Computing the sentiment
    scores = sid.polarity_scores(tweet_text)
    # Dictionary of sentiment scores. We are interested in scores['compund']
    return scores

def analyse_hashtag(hashtag, count):
    hashtag_sentiment_dict = defaultdict(list)
    twitter_api = api.TwitterAPI('api/credentials/twitter_credentials.json')
    tweets = twitter_api.searchByHashtag(hashtag=hashtag, count=count, lang='en', geocode=None, result_type='mixed')
    for tweet in tweets:
        sentiment_score = get_sentiment(tweet['full_text'])

        hashtag_sentiment_dict['hashtag'] = hashtag
        hashtag_sentiment_dict['value'].append((tweet['full_text'], tweet['created_at'], sentiment_score))
    return hashtag_sentiment_dict
        
if __name__ == "__main__":
    # Driver
    hashtagList = ['covid','football']
    hashtag_info_list = []
    for hashtag in hashtagList:
        hashtag_info_list.append(analyse_hashtag(hashtag, count=10))
    print(hashtag_info_list)