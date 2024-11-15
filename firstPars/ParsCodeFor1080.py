import pandas as pd
import re


file_path = r'CSV_FILE_PATH'
data = pd.read_csv(file_path)

def clean_comment_with_1080(comment):
    """
    Yorum metnini temizlemek için işlev.
    - '1080p' gibi yanlış çekilen verileri temizler, yalnızca '1080' anahtar kelimesini korur.
    - Tarih ve saat bilgilerini, gereksiz kullanıcı adlarını, URL'leri, fazlalık boşlukları ve gereksiz karakterleri temizler.
    """
    """
    1080 Ekran Kartlarını kazırken içeriğinde 1080p verilerini de çektiğini fark ettikten sonra içerisinde 1080p verisi olan kelimeleri tespit edip
    ayrı bir pars kodu yazıp temizletmem gerekti.

    """
    if '1080p' in comment:
        return None
    
    """
    re fonksiyonunu "https://docs.python.org/3/library/re.html" üzerinden alıntıladım ve kendi koduma entegre ettim
    """
    comment = re.sub(r'\d{2} \w+ \d{4} \d{2}:\d{2}:\d{2}', '', comment)
    comment = re.sub(r'\n+', ' ', comment) 
    comment = re.sub(r'http\S+|www\S+', '', comment)
    comment = re.sub(r'\w+ yazmış:', '', comment)
    comment = re.sub(r'Devamı için tıklayın...', '', comment)
    comment = re.sub(r'[^\w\s]', '', comment)
    comment = re.sub(r'\s+', ' ', comment).strip()
    
    return comment

data['Yorum Temiz'] = data['Yorum Temiz'].fillna('').apply(clean_comment_with_1080)
data_cleaned = data.dropna(subset=['Yorum Temiz']).reset_index(drop=True)

cleaned_file_path = r'SAVE_FILE_PATH'
data_cleaned[['Başlık', 'Yorum Temiz']].to_csv(cleaned_file_path, index=False)

print(f"Temizlenmiş veri '{cleaned_file_path}' dosyasına kaydedildi.")
