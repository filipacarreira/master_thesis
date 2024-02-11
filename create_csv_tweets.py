import os
from datetime import datetime
import pandas as pd
import json

input_path = ''

def get_tweets(location):
    """
    Takes a list of files with tweets and returns dataframe with created_at and text fields
    """
    files = os.listdir(f'{input_path}/json_files')
    list_text = []
    list_created = []
    for file in files:
        if file.startswith(location):
            with open(f'/data/filipac/thesis_data/json_files/{file}','r') as inputfile:
                tweets = [json.loads(line) for line in inputfile.read().splitlines()]
                for tweet in tweets:
                    print(tweet)
                    text = tweet['full_text']
                    created_at = tweet['created_at']
                    list_created.append(created_at)
                    list_text.append(text)
    pd.DataFrame({'created_at': list_created, 'tweet': list_text}).to_csv(f'tweets_{location}.csv')

get_tweets('IT')
get_tweets('PT')
get_tweets('NL')
get_tweets('DE')
get_tweets('FR')
get_tweets('GB')
