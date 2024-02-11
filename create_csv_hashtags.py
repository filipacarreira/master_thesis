import os
from datetime import datetime
import pandas as pd
import json

input_path = ""
def get_hashtags(location):
    """
    Takes a list of files with tweets and returns dataframe with created_at and hashtags fields
    """
    files = os.listdir(f'{input_path}/json_files')
    list_hash = []
    list_created = []
    for file in files:
        if file.startswith(location):
            with open(f'/data/filipac/thesis_data/json_files/{file}','r') as inputfile:
                tweets = [json.loads(line) for line in inputfile.read().splitlines()]
                for tweet in tweets:
                    hashtags = tweet['entities']['hashtags']
                    created_at = tweet['created_at']
                    list_created.append(created_at)
                    hashes = []
                    for hashtag in hashtags:
                        text = hashtag['text']
                        hashes.append(text)
                    list_hash.append(hashes)
    pd.DataFrame({'created_at': list_created, 'hashtags': list_hash}).to_csv(f'hashtags_{location}.csv')

get_hashtags('PT')
get_hashtags('IT')
get_hashtags('NL')
get_hashtags('DE')
get_hashtags('FR')
get_hashtags('GB')
