import pandas as pd
import re


file_path = r'CSV_FILE_PATH'
data = pd.read_csv(file_path)

def clean_comment(comment):
    
    """
    Yorum metnini temizlemek için işlev.
    - Tarih ve saat bilgilerini kaldırır.
    - URL, fazlalık boşluklar ve gereksiz karakterleri temizler.
    """

    comment = re.sub(r'\d{2} \w+ \d{4} \d{2}:\d{2}:\d{2}', '', comment)
    comment = re.sub(r'\n+', ' ', comment) 
    comment = re.sub(r'http\S+|www\S+', '', comment)
    comment = re.sub(r'\w+ yazmış:', '', comment)
    comment = re.sub(r'Devamı için tıklayın...', '', comment)
    comment = re.sub(r'[^\w\s]', '', comment)
    comment = re.sub(r'\s+', ' ', comment).strip()
    
    return comment


#Github üzerinden bir projeden bularak fillna fonksiyonunu buldum fakat repoyu kaynakça eklemek için bulamadım.
data['Yorum Temiz'] = data['Yorum'].fillna('').apply(clean_comment)
data_cleaned = data.dropna(subset=['Yorum Temiz']).reset_index(drop=True)


cleaned_file_path = '3050-Scrapping-Cleaned.csv' #İsteğe bağlı bir yol belirtilip de kayıt edilebilir! Şayet yapılmazsa programın çalıştığı dizine kaydeder
data_cleaned[['Başlık', 'Yorum Temiz']].to_csv(cleaned_file_path, index=False)

print(f"Temizlenmiş veri '{cleaned_file_path}' dosyasına kaydedildi.")
