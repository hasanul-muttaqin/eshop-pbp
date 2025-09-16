## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

    - langkah 1: menjalankan perintah 'django-admin startproject eshop_pbp' di directory eshop-pbp via windows powershell. langkah ini dilakukan untuk menyiapkan struktur projek(manage.py dan juga folder eshop_pbp yang berisi settings.py, urls.py, dll)

    - langkah 2: membuat aplikasi main dengan menjalankan 'python manage.py startapp main' di directory eshop_pbp dan kemudian menambahkan main ke eshop_pbp/settings.py agar aplikasi dikenali

    - langkah 3: import admin dari django.contrib serta import path & include dari django.urls lalu include main.urls untuk mengarahkan root ke */main/urls.py

    - langkah 4: import models dari django.db ke */main/models.py dan buat class product(yg extend class model) dengan attribut yang sudah ditentukan di tugas serta magic function __str__ yang mengembalikan nama

    - langkah 5: import render dari django.shortcuts dan import class product ke */main/views.py yang sudah diberikan tadi lalu buat fungsi main_view() yang return model yang sudah di-render

    - langkah 6: import path ke */main/urls.py dan routing ke fungsi main_view()

    - langkah 7: membuat main.html di template yang nantinya akan jadi template untuk di-render di web

    - langkah 8: melakukan fungsi 'python manage.py makemigrations' dan 'python manage.py migrate' untuk migrasi model ke template

    - langkah 9: login ke PWS dari situs PBP dan mengisi environs lalu push ke server dengan 'git push pws master'

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](AlurKerjaDjango.png)
    (source: https://scele.cs.ui.ac.id/mod/forum/discuss.php?d=57480)
    alur kerja django dimulai ketika pengguna mengirimkan HTTP(Hypertext Transfer Protocol) request, seperti contohnya ketika mengetik url lewat browser atau menekan link dari hypertext. selanjutnya, request pengguna diterima oleh urls.py. fungsi program urls.py adalah melakukan pencocokkan antara url request pengguna dan path yang sudah didefinisikan. jika ada path yang cocok, maka views.py akan dipanggil. fungsi dari views.py adalah sebagai otak utama dari halaman web yang akan ditampilkan. views.py melakukan ini dengan mengambil elemen yg telah terdefinisi di models.py dan menyusunnya mengikuti arahan yang tersedia di templates/main.html. kemudian, django akan mengirimkan HTTP response dalam bentuk HTML(hypertext markup language) ke browser pengguna.

## 3. Jelaskan peran settings.py dalam proyek Django!
### settings.py adalah konfigurasi pusat proyek. Perannya meliputi:

         Menentukan daftar aplikasi terpasang (INSTALLED_APPS).

        - Konfigurasi database (DATABASES).

        - Konfigurasi template (TEMPLATES) dan lokasi template directory.

        - Middleware yang aktif (MIDDLEWARE).

        - STATIC_URL, STATIC_ROOT, dan konfigurasi static files.

        - SECRET_KEY, DEBUG, ALLOWED_HOSTS.

        - Pengaturan i18n/l10n (bahasa dan zona waktu).

        - Pengaturan autentikasi, email, logging, dan konfigurasi pihak ketiga.

## 4. Bagaimana cara kerja migrasi database di Django?
    makemigrations: django akan mebuat file migrasi yang merepresentasikan perubahan model sebagai operasi CreateModel, AddField, AlterField, dll.
    migrate: operasi migrasi file dilakukan dengan mengikuti database tertera sehingga tabel mengikuti informasi di models.py

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    - Django memiliki banyak fitur built in

    - pola MTV yang sederhana sehingga lebih mudah dipahami

    - dokumentasi django yang mudah sehingga lebih mudah untuk pelajar dan pemula

    - keamanan dari banyak celah umum (CSRF, XSS, SQL injection)
    
    - komunitas dan ekosistem yang besar sehingga third party package dan tutorial

    - cocok untuk prototyping karena proses development yang cepat.

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    ga ada, slide sudah cukup jelas sehingga asistensi tidak terlalu diperlukan. tapi respons asdos cepat dalam menanggapi pertanyaan mahasiswa dan penjelasan yang diberikan mudah diikuti.

---

