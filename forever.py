#!/usr/bin/python3
from subprocess import Popen
import sys
import time
import os
from datetime import datetime
import pandas as pd

filename = sys.argv[1]
arg1 = sys.argv[2]
agr2 = sys.argv[3]

# Code of the city from where we want to extract tweets
code_city = agr2

########### Defining location ###########

location = pd.read_json('location.json', lines = 'True')

city = location[location['city'] == code_city].iloc[0]['city']
country = location[location['city'] == code_city].iloc[0]['country']

today = datetime.now()

# get month and day in the format MM and DD
if len(str(today.month)) == 1:
    month = str(0) + str(today.month)
else:
    month = str(today.month)

    
if len(str(today.day)) == 1:
    day = str(0) + str(today.day)
else:
    day = str(today.day)
    
process_name = f'{country}_{city}_{day}{month}{str(today.year)[2:]}'

count = 0 

while True:
    if count == 0: 
        os.system(f'echo {process_name}: Process started successfully at {datetime.now()} >> log_file.log')
    if count > 0:
        os.system(f'echo {process_name}: Process restarted successfully at {datetime.now()} >> log_file.log')

    # run the extraction file
    p = Popen("python3 " + filename + ' ' + arg1 + ' ' + agr2, shell=True)
    p.wait()
    # logs
    print(f'{process_name}: Process stopped at {datetime.now()}. Errors above:')
    os.system(f'echo {process_name}: Process stopped at {datetime.now()} >> log_file.log')
    os.system(f'echo =================================== >> log_file.log')
    count += 1
    time.sleep(5*60)