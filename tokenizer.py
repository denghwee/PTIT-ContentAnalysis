import pandas as pd
import pyvi
from pyvi import ViTokenizer

# Load the CSV file
df = pd.read_csv('C:/Users/ntrgi/Desktop/PTIT-ContentAnalysis-master/data/new_cmt.csv')

# Convert all entries in the comments column to strings, replacing NaN with an empty string
df['comment'] = df['comment'].astype(str).replace('nan', '', regex=True)

# Remove double quotes from the comments
df['comment'] = df['comment'].str.replace('"', '', regex=False)

# Tokenize the comments column using PyVi
tokenized_cmts = df['comment'].apply(lambda x: ViTokenizer.tokenize(x))

# Create a new DataFrame with the tokenized posts
tokenized_df = pd.DataFrame({'tokenized_cmt': tokenized_cmts})

# Save the tokenized data to a new CSV file
tokenized_df.to_csv('./data/tokenized_cmt.csv', index=False)