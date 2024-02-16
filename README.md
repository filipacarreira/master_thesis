# Master Thesis Repository

## Information
**Title:** Europe, your cities, your tweets - Digital European Identity through the eyes of the Twitter microblogging

**Abstract:**

Europe is home to a diverse array of cultures, economies, and demographics. Despite this, Europeans also maintain a shared sense of heritage and common values. This duality of diversity and similarity makes this group of countries a distinctive population to be studied. As such, this thesis seeks to identify the dimensions that connect and separate the European population.

To conduct our study, we gathered data from Twitter, since social media platforms have been widely used to shape societal behavior. Our analysis included 6 major European cities and covered a 8-month period to perform topic modeling and natural language processing. Our findings suggest that international topics exhibit similar levels of discourse intensity, while local topics are influenced by both location and the relationship between the city and the subject at hand.

This study not only enhances our comprehension of the European community but also initiates preliminary research toward establishing an empirically valid "European Digital Identity".

**Keywords**: Europe, Twitter, Topic Modeling, Natural Language Processing, BERTopic

**Link for the document** [here](https://run.unl.pt/handle/10362/163657)

**Final Grade: 19/20**
## Thesis Pipeline
![pipeline final cut](https://github.com/filipacarreira/master_thesis/assets/79151739/7e319c13-ad82-4a79-8513-851ca1806a01)

Files related with data extraction:
- [forever.py](https://github.com/filipacarreira/master_thesis/blob/main/forever.py)
- [twExt_v4.py](https://github.com/filipacarreira/master_thesis/blob/main/twExt_v4.py)
- [location.json](https://github.com/filipacarreira/master_thesis/blob/main/location.json)
- [tokens.json](https://github.com/filipacarreira/master_thesis/blob/main/tokens.json)

File related with duplicates removal:
- [create_json_files.py](https://github.com/filipacarreira/master_thesis/blob/main/create_json_files.py)

Files to create the final dataset and specific files with specific fields:
- All fields - [create_csv_all.py](https://github.com/filipacarreira/master_thesis/blob/main/create_csv_all.py)
- Hashtags - [create_csv_hashtags.py](https://github.com/filipacarreira/master_thesis/blob/main/create_csv_hashtags.py)
- Languages - [create_csv_lang.py](https://github.com/filipacarreira/master_thesis/blob/main/create_csv_lang.py)
- Tweets - [create_csv_tweets.py](https://github.com/filipacarreira/master_thesis/blob/main/create_csv_tweets.py)
- Users - [create_csv_users.py](https://github.com/filipacarreira/master_thesis/blob/main/create_csv_users.py)

Files related with topic modeling (using BERTopic):
- Create embeddings for half of the data, fit model and predict topics - [bertopic_loop.py](https://github.com/filipacarreira/master_thesis/blob/main/bertopic_loop.py)
- Predict topics for the other half of data - [bertopic_predict.py](https://github.com/filipacarreira/master_thesis/blob/main/bertopic_predict.py)
- Update topic representations - [update_topics.py](https://github.com/filipacarreira/master_thesis/blob/main/update_topics.py)
  
**BERTopic Pipeline**

![Tweets tese 2](https://github.com/filipacarreira/master_thesis/assets/79151739/879d242e-89e8-425f-b990-8d8755773549)

## About the extraction and how to use it:
Base code for extraction of geolocated Twitters
- This script will run continuously and extract tweets from a selected location (a city with a pre-defined radius from the center)
- In the command line run the command:
   - nohup python3 forever.py twExt_v4.py < name_token > < code_city > &
   - **nohup** - this command will allow for the script to run continuously
   - **forever.py** - is a file created to run continuously the script after, even if the script crashes
   - **name_token** - represents the name of the Developer account to use
   - **code_city** - represents the location from which we want to extract data
 - Options for **name_token** (in file [tokens.json](https://github.com/filipacarreira/master_thesis/blob/main/tokens.json)):
   - Flavio
   - Flavio_AR
   - Alberto
   - Vitor
   - Naomi
   - Marcel
   - Filipa
 - Options for **code_city** (in file [location.json](https://github.com/filipacarreira/master_thesis/blob/main/location.json)):
   - LX (Lisbon)
   - MI (Milano)
   - AMS (Amsterdam)
   - BER (Berlin)
   - PAR (Paris)
   - BCN (Barcelona)
   - LOND (London)
