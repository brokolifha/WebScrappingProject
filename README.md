
1)    WebScrapping Projesi

Bu proje, belirli bir ekran kartı modeline göre çeşitli web sitelerinden veri toplayarak bu verileri bir CSV dosyasına kaydeder. 
Toplanan veriler üzerinde tokenizasyon, stopword temizleme, lemmatizasyon ve kök bulma işlemleri gerçekleştirilir.
Her işlem, ayrı Python betikleriyle sırasıyla uygulanır.

2) Kullanılan Teknolojiler

   Programlama Dili: Python
   Geliştirme Ortamı: Visual Studio Code
   Kütüphaneler:
   `requests`: HTTP istekleri yapmak için kullanılır.
   `beautifulsoup4`: HTML ve XML dosyalarını ayrıştırmak için kullanılır.
   `pandas`: Veri analizi ve manipülasyonu için kullanılır.
   `nltk`: Doğal dil işleme görevleri için kullanılır.
   `re`: Düzenli ifadelerle metin işlemleri için kullanılır.

3) Kurulum

1. Proje dosyalarını bilgisayarınıza indirin veya terminal üzerinden aşağıdaki komutu kullanarak klonlayın:

   
   git clone https://github.com/brokolifha/WebScrappingProject.git
   

2. Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

   
   pip install requests beautifulsoup4 pandas nltk
   

4) Kullanım

   1) Web Kazıma İşlemi:

         `scrapping` dizinindeki `scraping_project.py` dosyasını açın.
         Web kazıma işlemi yapacağınız sitenin URL'sini, `scraping_project.py` dosyasındaki örnek linkin yerine yapıştırın.
         `page_num` değişkenine başlamak istediğiniz sayfa numarasını girin.
         Aranacak kelimeyi ve CSV dosyasının kaydedileceği yolu ve adını belirtin.
         Terminal üzerinden aşağıdaki komutu çalıştırarak işlemi başlatın:
         python scraping_project.py
     

      # İşlemi durdurmak için `CTRL + C` tuş kombinasyonunu kullanabilirsiniz.

   2) İlk Temizleme İşlemi:

         `firstPars` dizinindeki `ParsCode.py` dosyasını açın.
         Kazıma sonrası oluşturulan CSV dosyasının yolunu ve yeni oluşturulacak dosyanın kaydedileceği yolu belirtin.
         Terminal üzerinden aşağıdaki komutu çalıştırın:
         python ParsCode.py
     

   3) Tokenizasyon İşlemi:

       `tokenizasyon` dizinindeki `tokenizasyon.py` dosyasını açın.
       Parslanan CSV dosyasının yolunu ve tokenizasyon sonrası dosyanın kaydedileceği yolu belirtin.
      -Terminal üzerinden aşağıdaki komutu çalıştırın:
      python tokenizasyon.py
     

   4) Stopword Temizleme İşlemi:

      `stopWord` dizinindeki `stopWord.py` dosyasını açın.
      Tokenizasyon yapılan CSV dosyasının yolunu ve stopword temizleme sonrası dosyanın kaydedileceği yolu belirtin.
      Terminal üzerinden aşağıdaki komutu çalıştırın:
      python stopWord.py
     

   5) Lemmatizasyon İşlemi:

      `lemmatizasyon` dizinindeki `Lemmatizasyon.py` dosyasını açın.
      Stopword temizleme sonrası oluşturulan CSV dosyasının yolunu ve lemmatizasyon sonrası dosyanın kaydedileceği yolu belirtin.
      Terminal üzerinden aşağıdaki komutu çalıştırın:
      python Lemmatizasyon.py
  

   6) Kök Bulma İşlemi:

      `kokBulma` dizinindeki `kokBulma.py` dosyasını açın.
      Lemmatizasyon sonrası oluşturulan CSV dosyasının yolunu ve kök bulma işlemi sonrası dosyanın kaydedileceği yolu belirtin.
      Terminal üzerinden aşağıdaki komutu çalıştırın:
      python kokBulma.py
     

Her adımın sonunda, ilgili işlem tamamlandığında yeni bir CSV dosyası oluşturulacaktır. Bu dosyalar, bir sonraki işlem için kullanılacaktır.




