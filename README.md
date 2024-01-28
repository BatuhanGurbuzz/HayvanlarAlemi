# Hayvanlar Alemi Web Sitesi

Bu proje, Django ve Django Rest Framework kullanılarak geliştirilmiş bir hayvanlar alemi web sitesidir. Proje, hayvanların API'lerini çekmek ve göstermek için Django Rest Framework'ü kullanmaktadır.

## Özellikler

- Anasayfada en son eklenen 3 hayvanın görüntüsü.
- Tüm hayvanlar için tek bir sayfa altında liste ve sayfalama kullanımı.

## Kullanılan Teknolojiler

- Django
- Django Rest Framework

## Kurulum

1. Proje dosyalarını indirin.

   ```bash
   git clone https://github.com/kullanici/hayvanlar-alemi.git
2. Virtual environment'ı oluşturun ve aktif edin.
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux veya macOS
3. Gerekli bağımlılıkları yükleyin.
     ```bash
     pip install -r requirements.txt
4. Veritabanını migrate edin.
     ```bash
     python manage.py migrate
5. Sunucuyu başlatın.
     ```bash
     python manage.py runserver
