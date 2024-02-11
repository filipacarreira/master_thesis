import pandas as pd
import plotly.express as px
import pyLDAvis.gensim
# import gensim
import ast
import matplotlib.pyplot as plt
from bertopic import BERTopic
import pickle
import numpy as np
from hdbscan import HDBSCAN
from bertopic import BERTopic
from umap import UMAP
from sentence_transformers import SentenceTransformer
from bertopic.cluster import BaseCluster
from bertopic.vectorizers import ClassTfidfTransformer
import seaborn as sns

input_path = ""

# load embedding model
embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

####### load saved models #######
model_sep = BERTopic.load(
    f"{input_path}/embeddings/bertopic_sep",
    embedding_model=embedding_model)
model_oct = BERTopic.load(
    f"{input_path}/embeddings/bertopic_oct",
    embedding_model=embedding_model)
model_nov = BERTopic.load(
    f"{input_path}/embeddings/bertopic_nov",
    embedding_model=embedding_model)
model_dec = BERTopic.load(
    f"{input_path}/embeddings/bertopic_dec",
    embedding_model=embedding_model)
model_jan = BERTopic.load(
    f"{input_path}/embeddings/bertopic_jan",
    embedding_model=embedding_model)
model_feb = BERTopic.load(
    f"{input_path}/embeddings/bertopic_feb",
    embedding_model=embedding_model)
model_mar = BERTopic.load(
    f"{input_path}/embeddings/bertopic_mar",
    embedding_model=embedding_model)
model_apr = BERTopic.load(
    f"{input_path}/embeddings/bertopic_apr",
    embedding_model=embedding_model)

####### read saved embeddings (the half that was not fitted in the model) #######
####### predict for the half that wasn't fitted before #######
with open(f'{input_path}/embeddings/embeddings_complete50_sep2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_sep, probs_sep = model_sep.transform(stored_sentences, stored_embeddings)
df_topics_sep2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_sep})
print('processed september')

with open(f'{input_path}/embeddings/embeddings_complete50_oct2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_oct, probs_oct = model_oct.transform(stored_sentences, stored_embeddings)
df_topics_oct2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_oct})
print('processed october')

with open(f'{input_path}/embeddings/embeddings_complete50_nov2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_nov, probs_nov = model_nov.transform(stored_sentences, stored_embeddings)
df_topics_nov2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_nov})
print('processed november')

with open(f'{input_path}/embeddings/embeddings_complete50_dec2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_dec, probs_dec = model_dec.transform(stored_sentences, stored_embeddings)
df_topics_dec2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_dec})
print('processed december')

with open(f'{input_path}/embeddings/embeddings_complete50_jan2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_jan, probs_jan = model_jan.transform(stored_sentences, stored_embeddings)
df_topics_jan2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_jan})
print('processed january')

with open(f'{input_path}/embeddings/embeddings_complete50_feb2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_feb, probs_feb = model_feb.transform(stored_sentences, stored_embeddings)
df_topics_feb2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_feb})
print('processed february')

with open(f'{input_path}/embeddings/embeddings_complete50_mar2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_mar, probs_mar = model_mar.transform(stored_sentences, stored_embeddings)
df_topics_mar2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_mar})
print('processed march')

with open(f'{input_path}/embeddings/embeddings_complete50_apr2.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    stored_sentences = stored_data['tweet']
    stored_embeddings = stored_data['embeddings']
    stored_location = stored_data['location']
    stored_created = stored_data['created_at']
    stored_lang = stored_data['lang']

topics_apr, probs_apr = model_apr.transform(stored_sentences, stored_embeddings)
df_topics_apr2 = pd.DataFrame({"created_at": stored_created,'tweet': stored_sentences,'location': stored_location,'language': stored_lang,"topic": topics_apr})
print('processed april')

####### read saved tweets and corresponting topics #######
df_topics_sep = pd.read_csv(f'{input_path}/csv_files/df_topics_sep.csv', index_col=0)
df_topics_oct = pd.read_csv(f'{input_path}/csv_files/df_topics_oct.csv', index_col=0)
df_topics_nov = pd.read_csv(f'{input_path}/csv_files/df_topics_nov.csv', index_col=0)
df_topics_dec = pd.read_csv(f'{input_path}/csv_files/df_topics_dec.csv', index_col=0)
df_topics_jan = pd.read_csv(f'{input_path}/csv_files/df_topics_jan.csv', index_col=0)
df_topics_feb = pd.read_csv(f'{input_path}/csv_files/df_topics_feb.csv', index_col=0)
df_topics_mar = pd.read_csv(f'{input_path}/csv_files/df_topics_mar.csv', index_col=0)
df_topics_apr = pd.read_csv(f'{input_path}/csv_files/df_topics_apr.csv', index_col=0)

print('read other files')

####### concat all the tweets and corresponding topics #######
df_topics_sep_total = pd.concat([df_topics_sep, df_topics_sep2])
df_topics_oct_total = pd.concat([df_topics_oct, df_topics_oct2])
df_topics_nov_total = pd.concat([df_topics_nov, df_topics_nov2])
df_topics_dec_total = pd.concat([df_topics_dec, df_topics_dec2])
df_topics_jan_total = pd.concat([df_topics_jan, df_topics_jan2])
df_topics_feb_total = pd.concat([df_topics_feb, df_topics_feb2])
df_topics_mar_total = pd.concat([df_topics_mar, df_topics_mar2])
df_topics_apr_total = pd.concat([df_topics_apr, df_topics_apr2])

####### save the files #######
df_topics_sep_total.to_csv(f'{input_path}/csv_files/df_topics_sep_total.csv')
df_topics_oct_total.to_csv(f'{input_path}/csv_files/df_topics_oct_total.csv')
df_topics_nov_total.to_csv(f'{input_path}/csv_files/df_topics_nov_total.csv')
df_topics_dec_total.to_csv(f'{input_path}/csv_files/df_topics_dec_total.csv')
df_topics_jan_total.to_csv(f'{input_path}/csv_files/df_topics_jan_total.csv')
df_topics_feb_total.to_csv(f'{input_path}/csv_files/df_topics_feb_total.csv')
df_topics_mar_total.to_csv(f'{input_path}/csv_files/df_topics_mar_total.csv')
df_topics_apr_total.to_csv(f'{input_path}/csv_files/df_topics_apr_total.csv')

print('saved files')
