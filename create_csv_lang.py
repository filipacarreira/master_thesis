import os
from datetime import datetime
import pandas as pd
import json

input_path = ""

def get_location(location):
    """
    Takes a list of files with tweets and returns dataframe with language field
    """
    files = os.listdir(f'{input_path}/json_files')
    list_lang = []
    for file in files:
        if file.startswith(location):
            with open(f'/data/filipac/thesis_data/json_files/{file}','r') as inputfile:
                tweets = [json.loads(line) for line in inputfile.read().splitlines()]
                for tweet in tweets:
                    lang = tweet['lang']
                    list_lang.append(lang)

    pd.DataFrame(list_lang, columns=['lang']).to_csv(f'lang_{location}.csv')

get_location('PT')
get_location('IT')
get_location('NL')
get_location('DE')
get_location('FR')
get_location('GB')
