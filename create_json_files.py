import os
import sys
import tarfile
import json
import pandas as pd


### Inputs ###
location = sys.argv[1]
directory = ''
window_size = 3

def delete_dup(directory, window_size, location):
    """
    Given a directory, cleans the files of a given location to delete duplicated tweets
    Considers a given window of days to delete the files from, so that tweets that were extracted
    one day but still relative to the day before, for example, are not repeated
    """
    files = os.listdir(directory)
    os.makedirs(f'{directory}/json_files', exist_ok=True)

    # gets files of the desired location
    final_list = []
    for file in files:
        if file.startswith(location):
            final_list.append(file)

    # sorts the files per date
    final_list = sorted(final_list,key=lambda x: pd.to_datetime((x.split('_')[2]).split('.')[0], format='%d%m%y'))

    for i in range(len(final_list) - window_size + 1):
        window_files = final_list[i: i + window_size]
        middle_file = window_files[window_size // 2]

        output_file = f'{directory}/json_files/{middle_file}'
        processed_file = f'{directory}/{middle_file}.tmp'
        if not os.path.exists(output_file) and not os.path.exists(processed_file):
            date = middle_file.split('_')[2].split('.')[0]
            target_date = pd.to_datetime(date, format='%d%m%y')
            # create a set to store unique tweets
            unique_tweets = set()

            # open the input file and output file simultaneously
            for file in window_files:
                with open(f'{directory}/{file}', 'r') as in_file, open(f'{directory}/{file}.tmp', 'w') as out_file:
                    # iterate over each line and load it as a JSON object
                    for line in in_file:
                        try:
                            tweet = json.loads(line)
                            tweet_date = pd.to_datetime(tweet['created_at'], format='%a %b %d %H:%M:%S %z %Y')
                            # check if the tweet id is already in the list of tweets
                            if tweet_date.date() == target_date.date() and tweet['id'] not in unique_tweets:
                                # if it isn't, add it to the list and write the tweet to output file
                                unique_tweets.add(tweet['id'])
                                out_file.write(line)
                        except json.JSONDecodeError:
                            # ignores lines that are not valid
                            pass
            
            with open(f'{directory}/{middle_file}.tmp', 'r') as in_file, open(output_file, 'w') as out_file:
                for line in in_file:
                    out_file.write(line)

    files = os.listdir(directory)
    for file in files:
        if file.endswith('.tmp'):
            os.remove(f'{directory}/{file}')

delete_dup(directory = directory, window_size = window_size, location = location)