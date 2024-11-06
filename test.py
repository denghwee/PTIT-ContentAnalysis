import nltk
from nltk.corpus import stopwords
from pyvi import ViTokenizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Đây là một ví dụ về đoạn văn cần loại bỏ từ dừng."
stop_words_file = 'C:\\Users\\ntrgi\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\vietnamese\\vietnamese.txt'
stop_words = set(word.strip() for word in open(stop_words_file, encoding='utf-8'))

word_tokens = ViTokenizer.tokenize(text)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

print(" ".join(filtered_sentence))