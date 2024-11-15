import pandas as pd
from TurkishStemmer import TurkishStemmer

file_path = r"FILE_PATH"
df = pd.read_csv(file_path)

stemmer = TurkishStemmer()

#Zemberek kodlarını kullanamadığım için Github üzerinden TurkishStemmer adında bir repo buldum ve orada ki kodları kullanarak kök bulma işlemi yaptım.
#Repo : https://github.com/otuncelli/turkish-stemmer-python


def stem_text(text):
    if isinstance(text, str):
        return ' '.join([stemmer.stem(word) for word in text.split()])
    return text

for column in df.columns:
    if df[column].dtype == 'object':  
        df[column] = df[column].apply(stem_text)

output_path = r"SAVE_FILE_PATH"
df.to_csv(output_path, index=False)

print(f"Kök bulma işlemi tamamlandı: {output_path}")
