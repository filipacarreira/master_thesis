import os
from datetime import datetime
import pandas as pd
import json

input_path = ''

def get_users(location):
    """
    Takes a list of files with tweets and returns dataframe with users info: created_at, user, 
    verified, number of tweets and number of followers fields
    """
    files = os.listdir('/data/filipac/thesis_data/json_files')
    list_user = []
    list_verified = []
    list_followers = []
    list_count = []
    list_created = []
    for file in files:
        if file.startswith(location):
            with open(f'{input_path}/json_files/{file}','r') as inputfile:
                tweets = [json.loads(line, strict = False) for line in inputfile.read().splitlines()]
                for tweet in tweets:
                    created_at = tweet['created_at']
                    user = tweet['user']['screen_name']
                    verified = tweet['user']['verified']
                    followers = tweet['user']['followers_count']
                    count = tweet['user']['statuses_count']
                    list_user.append(user)
                    list_verified.append(verified)
                    list_followers.append(followers)
                    list_count.append(count)
                    list_created.append(created_at)

    pd.DataFrame({'created_at': list_created, 
                  'user': list_user, 
                  'verified': list_verified, 
                  'n_followers': list_followers,
                  'n_tweets': list_count}).to_csv(f'users_{location}.csv')

get_users('PT')
print('pt done')
get_users('IT')
print('it done')
get_users('NL')
print('nl done')
get_users('DE')
print('de done')
get_users('FR')
print('fr done')
get_users('GB')
print('gb done')
