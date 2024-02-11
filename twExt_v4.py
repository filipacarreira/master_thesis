#!/usr/bin/python

import tweepy
import pandas as pd
import json
from datetime import datetime
import time
import sys
import os
import glob
import csv

# Name of the person of the token we're using
name_token = sys.argv[1]

# Code of the city from where we want to extract tweets
code_city = sys.argv[2]

########### Connecting to API ###########

token = pd.read_json('tokens.json', lines = 'True')

consumer_key = token[token['name'] == name_token].iloc[0]['consumer_key']
consumer_secret = token[token['name'] == name_token].iloc[0]['consumer_secret']
access_token = token[token['name'] == name_token].iloc[0]['access_token']
access_token_secret = token[token['name'] == name_token].iloc[0]['access_token_secret']

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret,
   access_token, access_token_secret
)
api = tweepy.API(auth)

########### Defining location ###########

location = pd.read_json('location.json', lines = 'True')

city = location[location['city'] == code_city].iloc[0]['city']
country = location[location['city'] == code_city].iloc[0]['country']
coord = location[location['city'] == code_city].iloc[0]['coord']
radius = location[location['city'] == code_city].iloc[0]['radius']

########### Extracting Tweets ###########

count = 0
today = datetime.now()
count_day = 0
aux = 0

while True:
    if today.strftime("%d/%m/%Y") != datetime.today().strftime("%d/%m/%Y"):
        count_day = 0
        with open ("daily_tweets"+".csv",'a') as filedata:                            
            writer = csv.DictWriter(filedata, delimiter=',', fieldnames=['Date', 'Location', 'Number of tweets'])
            writer.writerow({'Date':today.strftime("%d/%m/%Y"),'Location':city,'Number of tweets':len(pd.read_json(fname, lines = True))})
        files_list = glob.glob(f'{country}_{city}_*.json')
        count_tweets = 0
        for file in files_list:
            count_tweets += sum(1 for line in open(file))
            #len(pd.read_json(file, lines = True))
        os.system(f'echo  === Date: {today} === >> total_tweets.log')
        os.system(f'echo {city} - Total tweets extracted: {count_tweets} >> total_tweets.log')
        os.system(f'echo =================================== >> total_tweets.log')
        
    today = datetime.now()
    if len(str(today.month)) == 1:
        month = str(0) + str(today.month)
    else:
        month = str(today.month)
        
    if len(str(today.day)) == 1:
        day = str(0) + str(today.day)
    else:
        day = str(today.day)
        
    process_name = f'{country}_{city}_{day}{month}{str(today.year)[2:]}'
    
    try:
        auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_token, access_token_secret
                )
        api = tweepy.API(auth)
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")
        os.system(f'echo {process_name} - Authentication error at {datetime.now()} >> log_file.log')
        time.sleep(5*60)
        pass

    n=730

    if count == 0:
        os.system(f'echo {process_name} - Started extracting tweets at {datetime.now()} >> log_file.log')
        tweets=tweepy.Cursor(api.search_tweets,q="",geocode=coord+','+radius,tweet_mode="extended").items(n)
        
    else:
        tweets=tweepy.Cursor(api.search_tweets,q="",geocode=coord+','+radius, since_id = aux , tweet_mode="extended").items(n)
 
    fname = f'{country}_{city}_{day}{month}{str(today.year)[2:]}.json'

    aux = 0
    with open(fname, 'a') as outfile:
        for tweet in tweets:
            outfile.write(json.dumps(tweet._json))
            outfile.write('\n')
            if tweet.id > aux:
                aux = tweet.id
        outfile.close()
    count += 1
    count_day += 1

    if count % 4 == 0:
        os.system(f'echo {process_name} - Process was running correctly at {datetime.now()} >> log_file.log')
        os.system(f'echo {process_name} - Total tweets extracted today: {len(pd.read_json(fname, lines = True))} >> log_file.log')
        os.system(f'echo {process_name} - Total runs of process: {count} >> log_file.log')
        os.system(f'echo {process_name} - Total runs of the day: {count_day} >> log_file.log')
        os.system(f'echo =================================== >> log_file.log')

    time.sleep(15*60)