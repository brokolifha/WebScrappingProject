import pandas as pd
from nltk.tokenize import word_tokenize



"""
tokenizasyon,stopword ve Lemmatizing işlemlerinde ki kodları belirttiğim kaynaktan buldum direkt kopyalamadım ama kendi projemde kullanabilir hale getirdim 
https://realpython.com/nltk-nlp-python/
"""

file_path = 'CSV-FILE_PATH'
df = pd.read_csv(file_path)

def tokenize_text_nltk(text):
    tokens = word_tokenize(str(text).lower())
    return ' '.join(tokens) 

for column in df.columns:
    if df[column].dtype == "object": 
        df[column] = df[column].apply(tokenize_text_nltk)

output_path = 'SAVE_FILE_PATH'
df.to_csv(output_path, index=False)
print(f"Tokenize edilmiş veri: {output_path}")
