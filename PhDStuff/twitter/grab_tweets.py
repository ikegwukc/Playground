from twython import Twython
import json
import os
import pandas as pd

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'crude oil',
        'result_type': 'popular',
        'count': 100,
        'lang': 'en',
        }

# Search tweets
dict_ = {'text': [], 'sentiment': []}
for status in python_tweets.search(**query, tweet_mode='extended')['statuses']:
    #print(status.keys())
    dict_['text'].append(status['full_text'].replace('\n', ' '))
    dict_['sentiment'].append('+')


# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.head(5)
print('Wrote to tweets.csv')
df.to_csv('tweets.csv', sep='\t', index=False)
