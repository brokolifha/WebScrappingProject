import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import csv
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#Alıntılanmış kod,
#https://www.selenium.dev/documentation/
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.set_capability('acceptInsecureCerts', True)
    
    driver_path = r'C:\Drivers\chromedriver-win64\chromedriver.exe'
    service = Service(driver_path)
    
    return webdriver.Chrome(service=service, options=chrome_options)



def scrape_thread_comments(driver):
    try:
        WebDriverWait(driver, random.randint(40, 65)).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-content')))
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        comments = soup.find_all('div', class_='message-content')
        
        
        page_comments = [comment.text.strip() for comment in comments]
        return page_comments
    except TimeoutException:
        logging.error("Sayfa yükleme süresi doldu.")
        return []
    except Exception as e:
        logging.error(f"Yorumları alırken hata: {e}")
        return []

def scrape_page(url, driver, keyword):
    try:
        driver.get(url)
        WebDriverWait(driver, random.randint(45,100)).until(EC.presence_of_element_located((By.CLASS_NAME, 'structItem-title'))) 
        time.sleep(random.randint(15,60)) 
        
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        threads = soup.find_all('div', class_='structItem-title') 

        page_comments = []
        keyword_found = False

        for thread in threads:
            if keyword.lower() in thread.text.lower(): 
                keyword_found = True
                thread_title = thread.text.strip()
                
                logging.info(f"Bulunan başlık: {thread_title}")

                
                thread_url = thread.find('a').get('href')
                if not thread_url.startswith('http'):
                    full_thread_url = f"https://forum.donanimarsivi.com{thread_url}"
                else:
                    full_thread_url = thread_url
                
                driver.get(full_thread_url)
                time.sleep(random.randint(15, 60)) 

                comments = scrape_thread_comments(driver)
                if comments:
                    page_comments.append((thread_title, comments)) 

                
                driver.back()
                time.sleep(random.randint(15, 60))

        if not keyword_found:
            logging.info(f"Anahtar kelime '{keyword}' sayfada bulunamadı.")

        return page_comments, keyword_found

    except Exception as e:
        logging.error(f"Sayfa alırken hata: {e}")
        return None, False


base_url = 'https://forum.donanimarsivi.com/forumlar/ekran-karti.43/' #En son veriler donanımarsivi.com üzerinden çekildiği için bir örnek olarak bırakılmıştır.
page_url = f'{base_url}page-{{}}'


page_num = 2  
all_comments = []
successful_pages = []
keyword = "3050" 

driver = create_driver()


#Birebir alıntı kod değil fakat direkt olarak iki kaynaktan bulduklarımı kullandım,
#https://docs.python.org/3/library/csv.html
#https://www.w3schools.com/python/pandas/pandas_csv.asp
with open('4070-Scrapping.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Başlık", "Yorum"]) 


    try:
        while True:
            url = page_url.format(page_num)
            logging.info(f"Veri çekiliyor: {url}")
            
            try:
                page_comments, keyword_found = scrape_page(url, driver, keyword)
                
                if page_comments is None:
                    logging.warning(f"Sayfa {page_num} için veri toplanamadı. WebDriver'ı yeniden başlatılıyor.")
                    driver.quit()
                    driver = create_driver()
                    continue
                
                if not keyword_found:
                    logging.info(f"'{keyword}' thread'lerde bulunamadı. Sonraki sayfaya geçiliyor.")
                    page_num += 1
                    continue
                
                if not page_comments:
                    logging.info(f"Sayfa {page_num} bulunamadı veya boş. Döngü durduruluyor.")
                    break
                
                all_comments.extend(page_comments)
                successful_pages.append(page_num)
                logging.info(f"Sayfa {page_num}'den {len(page_comments)} yorum toplandı.")
                
                
                #Birebir alıntı değil ama yukarı da ki csv dökümanlarından bakılarak yazıldı!
                for title, comments in page_comments:
                    writer.writerow([title])  
                    for comment in comments:
                        writer.writerow(["", comment]) 

            except WebDriverException:
                logging.error(f"WebDriver hatası. WebDriver yeniden başlatılıyor.")
                driver.quit()
                driver = create_driver()
                continue
            
            page_num += 1  
            
        
            if page_num % 10 == 0:
                logging.info("Planlı WebDriver yeniden başlatılıyor.")
                driver.quit()
                driver = create_driver()

        
            time.sleep(random.randint(15, 45))

    except Exception as e:
        logging.error(f"Beklenmeyen hata: {e}")

    finally:
        driver.quit()

logging.info(f"Scraping tamamlandı. Toplam yorum sayısı: {len(all_comments)}")
logging.info(f"Başarıyla çekilen sayfalar: {successful_pages}")
logging.info("Veri 4070-Scrapping.csv dosyasına kaydedildi.")
