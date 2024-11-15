import pandas as pd

file_names = [
    "1050-Scrapping-Cleaned.csv", "1060-Scrapping-Cleaned.csv", "1070-Scrapping-Cleaned.csv", 
    "1080-Scrapping-Cleaned.csv", "2050-Scrapping-Cleaned.csv", "2060-Scrapping-Cleaned.csv", 
    "2070-Scrapping-Cleaned.csv", "2080-Scrapping-Cleaned.csv", "3050-Scrapping-Cleaned.csv", 
    "3060-Scrapping-Cleaned.csv", "3070-Scrapping-Cleaned.csv", "3080-Scrapping-Cleaned.csv", 
    "3090-Scrapping-Cleaned.csv", "4050-Scrapping-Cleaned.csv", "4060-Scrapping-Cleaned.csv", 
    "4070-Scrapping-Cleaned.csv", "4080-Scrapping-Cleaned.csv", "4090-Scrapping-Cleaned.csv"
]


#Diğer kodlarda da belirttiğim gibi direkt olarak alıntı bir kod satırı değildir fakat dökümandan bulunup kullanılmıştır. "concat"
all_data = pd.concat([pd.read_csv(file, encoding='utf-8') for file in file_names])

all_data.to_csv("All_Scrapping_Cleaned.csv", index=False, encoding='utf-8')

print("Toplam veri sayısı:", len(all_data))
