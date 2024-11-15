import pandas as pd
from nltk.corpus import stopwords
import nltk


nltk.download('stopwords')

"""
tokenizasyon,stopword ve Lemmatizing işlemlerinde ki kodları belirttiğim kaynaktan buldum direkt kopyalamadım ama kendi projemde kullanabilir hale getirdim 
https://realpython.com/nltk-nlp-python/
"""


file_path = r'FILE_PATH'
df = pd.read_csv(file_path)


stop_words = set(stopwords.words("turkish"))


def remove_stopwords(tokens):
    tokens_list = eval(tokens) if isinstance(tokens, str) else tokens
    return [token for token in tokens_list if token not in stop_words]

if 'Başlık_tokenized' in df.columns:
    df['Başlık_tokenized'] = df['Başlık_tokenized'].apply(lambda x: remove_stopwords(eval(x)) if isinstance(x, str) else x)
if 'Yorum Temiz_tokenized' in df.columns:
    df['Yorum Temiz_tokenized'] = df['Yorum Temiz_tokenized'].apply(lambda x: remove_stopwords(eval(x)) if isinstance(x, str) else x)

output_path = r'SAVE_FILE_PATH'
df.to_csv(output_path, index=False)
print(f"Stopwords temizlenmiş veri: {output_path}")
