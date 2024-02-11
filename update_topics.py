import pandas as pd
from bertopic.vectorizers import ClassTfidfTransformer
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic


input_path = ''

# get original topics
df_topics_sep = pd.read_csv(f'{input_path}/csv_files/df_topics_sep.csv', index_col=0)
df_topics_oct = pd.read_csv(f'{input_path}/csv_files/df_topics_oct.csv', index_col=0)
df_topics_nov = pd.read_csv(f'{input_path}/csv_files/df_topics_nov.csv', index_col=0)
df_topics_dec = pd.read_csv(f'{input_path}/csv_files/df_topics_dec.csv', index_col=0)
df_topics_jan = pd.read_csv(f'{input_path}/csv_files/df_topics_jan.csv', index_col=0)
df_topics_feb = pd.read_csv(f'{input_path}/csv_files/df_topics_feb.csv', index_col=0)
df_topics_mar = pd.read_csv(f'{input_path}/csv_files/df_topics_mar.csv', index_col=0)
df_topics_apr = pd.read_csv(f'{input_path}/csv_files/df_topics_apr.csv', index_col=0)
print('got topics')

# load saved models
embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
model_sep = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_sep",
    embedding_model=embedding_model)
model_oct = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_oct",
    embedding_model=embedding_model)
model_nov = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_nov",
    embedding_model=embedding_model)
model_dec = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_dec",
    embedding_model=embedding_model)
model_jan = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_jan",
    embedding_model=embedding_model)
model_feb = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_feb",
    embedding_model=embedding_model)
model_mar = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_mar",
    embedding_model=embedding_model)
model_apr = BERTopic.load(
    "/data/filipac/thesis_data/embeddings/bertopic_apr",
    embedding_model=embedding_model)
print('got models')

# update topics to delete stop words
ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
model_sep.update_topics(df_topics_sep['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_oct.update_topics(df_topics_oct['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_nov.update_topics(df_topics_nov['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_dec.update_topics(df_topics_dec['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_jan.update_topics(df_topics_jan['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_feb.update_topics(df_topics_feb['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_mar.update_topics(df_topics_mar['tweet'].to_list(), ctfidf_model=ctfidf_model)
model_apr.update_topics(df_topics_apr['tweet'].to_list(), ctfidf_model=ctfidf_model)
print('updated topics')

# save topics
model_sep.save(f"{input_path}/embeddings/bertopic_sep_updated_topics",serialization="safetensors",save_ctfidf=True)
model_oct.save(f"{input_path}/embeddings/bertopic_oct_updated_topics",serialization="safetensors",save_ctfidf=True)
model_nov.save(f"{input_path}/embeddings/bertopic_nov_updated_topics",serialization="safetensors",save_ctfidf=True)
model_dec.save(f"{input_path}/embeddings/bertopic_dec_updated_topics",serialization="safetensors",save_ctfidf=True)
model_jan.save(f"{input_path}/embeddings/bertopic_jan_updated_topics",serialization="safetensors",save_ctfidf=True)
model_feb.save(f"{input_path}/embeddings/bertopic_feb_updated_topics",serialization="safetensors",save_ctfidf=True)
model_mar.save(f"{input_path}/embeddings/bertopic_mar_updated_topics",serialization="safetensors",save_ctfidf=True)
model_apr.save(f"{input_path}/embeddings/bertopic_apr_updated_topics",serialization="safetensors",save_ctfidf=True)
print('saved topics')