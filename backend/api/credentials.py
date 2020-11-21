import json
import os

PATH = 'credentials'

# Create a dictionary to store your twitter credentials
twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
twitter_cred['CONSUMER_KEY'] = '********'
twitter_cred['CONSUMER_SECRET'] = '********'
twitter_cred['ACCESS_TOKEN'] = '********'
twitter_cred['ACCESS_TOKEN_SECRET'] = '********'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public
if not os.path.isdir(PATH):
    os.mkdir(PATH)
filePath = os.path.join(PATH, 'twitter_credentials.json')
if not os.path.isfile(filePath):
    with open(filePath, 'w') as secret_info:
        json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)