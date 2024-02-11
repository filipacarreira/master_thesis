import os
from datetime import datetime
import pandas as pd
import json

input_path = ""

def get_df(location):
    """
    Takes a list of files with tweets and returns dataframe with created_at, text, language and hashtags fields
    """
    files = os.listdir(f'{input_path}/json_files')
    list_hash = []
    list_created = []
    list_lang = []
    list_user = []
    list_verified = []
    list_followers = []
    list_count = []
    list_text = []
    for file in files:
        if file.startswith(location):
            with open(f'/data/filipac/thesis_data/json_files/{file}','r') as inputfile:
                tweets = [json.loads(line) for line in inputfile.read().splitlines()]
                for tweet in tweets:
                    hashtags = tweet['entities']['hashtags']
                    created_at = tweet['created_at']
                    text = tweet['full_text']
                    lang = tweet['lang']
                    user = tweet['user']['screen_name']
                    verified = tweet['user']['verified']
                    followers = tweet['user']['followers_count']
                    count = tweet['user']['statuses_count']
                    list_created.append(created_at)
                    list_lang.append(lang)
                    list_user.append(user)
                    list_verified.append(verified)
                    list_followers.append(followers)
                    list_count.append(count)
                    list_text.append(text)
                    hashes = []
                    for hashtag in hashtags:
                        text = hashtag['text']
                        hashes.append(text)
                    list_hash.append(hashes)
    pd.DataFrame({
        'created_at': list_created,
        'tweet': list_text,
        'hashtags': list_hash,
        'lang': list_lang,
        'user': list_user,
        'n_followers': list_followers,
        'n_tweets': list_count,
        'verified': list_verified
        }).to_csv(f'csv_files/complete_{location}.csv')

get_df('IT')
print('it done')
get_df('PT')
print('pt done')
get_df('NL')
print('nl done')
get_df('DE')
print('de done')
get_df('FR')
print('fr done')
get_df('GB')
print('gb done')