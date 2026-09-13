# CourseApp

![Django](https://img.shields.io/badge/Django-5.1-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red)

CourseApp, Django ile geliştirilmiş çevrimiçi öğrenme platformudur. Kullanıcılar kursları listeleyip detaylarını görüntüleyebilir; eğitmenler kendi kurslarını oluşturup yönetebilir.

## Özellikler

- **Kullanıcı kimlik doğrulama** — Django'nun yerleşik sistemiyle kayıt ve giriş
- **Kurs yönetimi** — kurs ekleme, güncelleme, silme ve kapak görseli yükleme
- **Kategori sistemi** — kurslar kategorilere göre organize edilir, kategoriler dinamik olarak oluşturulabilir
- **Etiket sistemi** — kurslara birden fazla etiket atanabilir; kategori ve etikete göre listeleme
- **Eğitmen paneli** — eğitmenler kendi kurslarını yönetir
- **Admin paneli** — Django admin üzerinden içerik yönetimi
- **Duyarlı tasarım** — mobil, tablet ve masaüstü uyumlu arayüz (Bootstrap 5)

## Kullanılan Teknolojiler

| Katman | Teknoloji |
| --- | --- |
| Backend | Python 3.13, Django 5.1 |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Veritabanı | SQLite (varsayılan) |
| Görsel işleme | Pillow — kurs kapak görselleri |

## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/fatihdogann/CourseApp.git
   cd CourseApp
   ```

2. Sanal ortam oluşturun ve etkinleştirin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Veritabanı migration'larını uygulayın:

   ```bash
   python manage.py migrate
   ```

5. Yönetici hesabı oluşturun:

   ```bash
   python manage.py createsuperuser
   ```

6. Geliştirme sunucusunu başlatın:

   ```bash
   python manage.py runserver
   ```

Uygulama `http://127.0.0.1:8000` adresinde çalışır; admin paneli `/admin/` yolundadır.

## Proje Yapısı

```
CourseApp/
├── accounts/              # Kayıt / giriş görünümleri ve formları
├── courses/               # Kurs, kategori ve etiket modelleri; görünümler
├── pages/                 # Ana sayfa ve statik sayfalar
├── courseapp/             # Django proje ayarları
├── templates/             # Temel şablonlar ve yeniden kullanılabilir parçalar
├── static/                # CSS, JavaScript ve görseller
├── Ekran Görüntüleri/     # README ekran görüntüleri
├── manage.py
└── requirements.txt
```

## Ekran Görüntüleri

### Ana Sayfa

![Ana Sayfa](Ekran%20G%C3%B6r%C3%BCnt%C3%BCleri/CourseApp-1.png)

### Kurs Sayfası

![Kurs Sayfası](Ekran%20G%C3%B6r%C3%BCnt%C3%BCleri/CourseApp-2.png)

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

## Geliştirici

**Mehmet Fatih Doğan** — backend geliştirici, güvenlik meraklısı.

- 🌐 Portfolyo & iletişim: [mehmetfatihdogan.com.tr](https://mehmetfatihdogan.com.tr)
- 💻 GitHub: [@fatihdogann](https://github.com/fatihdogann)

Proje hakkında soru, hata bildirimi veya geri bildirim için [iletişim sayfamdan](https://mehmetfatihdogan.com.tr/iletisim) ulaşabilirsin.
