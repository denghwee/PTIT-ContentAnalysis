import nltk
import pandas as pd

with open('./vietnamese-stopwords.txt', encoding='utf-8') as f:
  stop_words = set(f.read().splitlines())

df = pd.read_csv('./data/tokenized_output.csv')

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

df['filtered_tokens'] = df['tokenized_post'].apply(remove_stopwords)

# Lưu kết quả vào file mới
df.to_csv('./data/filtered_output.csv', index=False)
