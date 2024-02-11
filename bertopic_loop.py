from sklearn.decomposition import PCA
from hdbscan import HDBSCAN
import pandas as pd
from bertopic import BERTopic
import numpy as np
from umap import UMAP
import time
import pickle
import random
from sentence_transformers import SentenceTransformer


print('++++++++++++++++ BERTopic ++++++++++++++++')
start_time = time.time()
input_path = ""
df = pd.read_csv(f'{input_path}/final_europe.csv', index_col = 0)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
df = df[~(df['created_at'].str.startswith('['))]

print("--- %s seconds ---" % (time.time() - start_time))

list_months = ['Sep', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']

for month in list_months:
    print(f'++++ Started {month} ++++')

    df_month = df[df['created_at'].str.contains(month)]

    print('read and filtered df')
    print(f'number of tweets before removing: {len(df_month)}')

    # group data by day
    df_month['created_at'] = pd.to_datetime(df_month['created_at'])
    df_month['created_date'] = df_month['created_at'].dt.date
    grouped_data = df_month.groupby('created_date')

    sampled_data = pd.DataFrame(columns=df_month.columns)

    # delete 50% of the tweets equally from each day
    for day, group in grouped_data:
        # see how many tweets to delete
        num_records = len(group)
        num_to_delete = int(num_records * 0.5)
        
        # randomly select tweets
        indices_to_delete = random.sample(list(group.index), num_to_delete)
        
        # delete tweets from the sampled data
        group_to_delete = group.loc[indices_to_delete]
        
        # append the records to delete to the sampled_data DataFrame
        sampled_data = pd.concat([sampled_data, group_to_delete])

    # drop the sampled data from the filtered data
    df_month = df_month.drop(sampled_data.index)

    print('got reduced dataframe')
    print(f'number of tweets after removing: {len(df_month)}')
    tweets = df_month['tweet'].to_list()

    # pre-calculate embeddings
    print(f'started embeddings')
    embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    embeddings = embedding_model.encode(tweets, show_progress_bar=True)
    print('finished embeddings')

    # save embeddings
    with open(f'{input_path}/embeddings/embeddings_complete50_{month}.pkl', "wb") as fOut:
        pickle.dump({
            'created_at': df_month['created_at'].to_list(),
            'tweet': tweets,
            'hashtags': df_month['hashtags'].to_list(),
            'lang': df_month['lang'].to_list(),
            'user': df_month['user'].to_list(),
            'location': df_month['location'].to_list(),
            'embeddings': embeddings,
            }, fOut, protocol=pickle.HIGHEST_PROTOCOL)

    print('saved embeddings')

    umap_model = UMAP(
        n_neighbors=15,
        n_components=5,
        min_dist=0.0,
        metric="cosine",
        verbose = True
        # init = pca_embeddings
    )
    reduced_embeddings_2d = umap_model.fit_transform(embeddings)

    class Dimensionality:
        """ Use this for pre-calculated reduced embeddings """
        def __init__(self, reduced_embeddings):
            self.reduced_embeddings = reduced_embeddings

        def fit(self, X):
            return self

        def transform(self, X):
            return self.reduced_embeddings

    umap_model = Dimensionality(reduced_embeddings_2d)

    hdbscan_model = HDBSCAN(
        min_cluster_size=150, 
        metric='euclidean', 
        cluster_selection_method='eom', 
        prediction_data=True
    )

    topic_model = BERTopic(
        verbose = True,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        calculate_probabilities=False
    )

    start_time = time.time()
    topics, probs = topic_model.fit_transform(tweets, embeddings = embeddings)
    print('finished fitting')
    print("--- %s seconds ---" % (time.time() - start_time))

    topic_model.save(
        f"{input_path}/embeddings/bertopic_{month}",
        serialization="safetensors",
        save_ctfidf=True
    )
    print('saved model')

    df = pd.DataFrame({"created_at": df_month['created_at'].to_list(),
                    'tweet': tweets,
                    'location': df_month['location'].to_list(),
                    'language': df_month['lang'].to_list(),
                    "topic": topics})
    df.to_csv(f'{input_path}/csv_files/df_topics_{month}.csv')
    print('saved dataframe')
    print(f'++++++ finished {month} ++++++')

print('saved models')
print('++++++++++++++++++++++++++++++++++++++++++')
