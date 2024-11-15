import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re

nltk.download('wordnet')
nltk.download('omw-1.4')

file_path = r"FILE_PATH"
df = pd.read_csv(file_path)

#SpaCy yükleyemediğim için nltk kütüphanesini kullanmak zorunda kaldım. Java üzerinden githubdan zemberek kodları indirerek onları çalıştırmayı denedim yine olmadı.
"""
tokenizasyon,stopword ve Lemmatizing işlemlerinde ki kodları belirttiğim kaynaktan buldum direkt kopyalamadım ama kendi projemde kullanabilir hale getirdim 
https://realpython.com/nltk-nlp-python/
"""

lemmatizer = WordNetLemmatizer()

for column in df.columns:
    if df[column].dtype == 'object': 
        df[column] = df[column].apply(clean_and_lemmatize)

output_path = r"SAVE_FILE_PATH"
df.to_csv(output_path, index=False)

print(f"Lemmatization ve temizlik işlemi tamamlandı: {output_path}")
