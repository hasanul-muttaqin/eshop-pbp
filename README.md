# Tugas 1

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

# Tugas 2

## 1. Mengapa kita memerlukan data delivery dalam pengimplementasian platform?
### Ada beberapa alasan mengapa data delivery diperlukan dalam implementasi platform
- komunikasi antar komponen: front-end butuh data dari back-end agar UI bisa ditampilkan
- skalabilitas: pemisahan front-end dan back-end memungkinkan development terpisah sehingga skalabilitas lebih mudah
- interoperabilitas: third party integration lebih mudah dengan format data JSON/XML
- Performa & pengalaman pengguna: data yang dikirim terstruktur memungkinkan caching, partial updates (AJAX), lazy loading, sehingga UX lebih responsif.
- Keamanan & kontrol akses: pengiriman terstruktur memudahkan otentikasi, otorisasi, rate-limiting, logging.
- Versi & backward compatibility: API versioning memudahkan migrasi tanpa memecah klien lama.
- Real-time & notifikasi: websocket/sse memungkinkan push data untuk fitur chat/live updates.

## 2.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
menurut saya lebih baik JSON, alasan JSON lebih popular ialah sebagai berikut:
- lebih ringan
- lebih mudah parsing ke JS karena native
- mendukung tipe data yang lebih banyak. seperti number, string, boolean, array, object, etc
- lebih bagus untuk data terstruktur karena variasi tipe data
- readability lebih bagus
- terhubung ke ekosistem java dan JS yang extensive(contoh, RESTful API)

## 3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
fungsi is_valid()
- Memicu proses full_clean di form
    - Validasi field-by-field (field validators, tipe data, required, min/max).
    - Panggil clean_<field>() custom jika ada.
    - Panggil clean() form-level untuk cross-field checks.
- Mengisi form.cleaned_data (versi data yang sudah dibersihkan/di-cast).
- Mengisi form.errors jika ada error.
- Mengembalikan True jika semua valid, False jika ada error.
##### fungsi: mencegah tipe data salah, menyediakan forms.error untuk user, membersihkan data untuk mencegah masalah keamanan seperti SQL inject, mencegah exception

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

#### fungsi:
- Django meletakkan token unik per sesi (atau cookie) dan memverifikasinya pada request POST/PUT/DELETE yang diterima.
- Jika token tidak cocok/absent, middleware Django menolak request mencegah tindakan atas nama pengguna tanpa izin.
#### risiko tidak memakai CSRF token
- inject laman jahat untuk menggunakan sesi pengguna lain
- korupsi data oleh sistem
- privilege escalation oleh attacker
- akses yang tidak diauthorisasi

## 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. keempat fungsi dibuat dengan menggunakan fungsi bawaan serialize dari Django.core. untuk show_xml() dan show_json() sebenarnya sangan mirip dengan grab semua object product .all() dan kemudian di serialize ke xml atau json, sedangkan untuk kedua fungsi ..._by_id() menggunakan variable baru products_id, yang nantinya akan digunakan untuk menjalankan fungsi .get() untuk mengambil data produk spesifik, kemudian di-wrap dalam list agar bisa di-serialize
2. dalam urls.py ditambahkan path /json dan /xml yang nantinya akan memanggil fungsi show_xml() dan show_json() untuk menampilkan semua product dalam template masing masing. dibuat juga path /xml/<str:products_id> dan /json/<str:products_id> yang akan memanggil masing-masing fungsi by id dengan menggunakan nilai yang diinput di url sebagai variable input products_id untuk fungsi
3. menambahkan button add di main/html yang route ke path /create-products dan juga jika tidak ada product akan muncul hyperlink 'add one' yang routing ke path yg sama. kemudian ada juga tombol 'Detail' dan on-click di card product yang routing ke /products/<id>
4. method create_products() di views.py memanggil forms.py lalu render create_products.html, yang memiliki input field untuk isi forms.py, dengan menekan button 'add product' user akan dikembalikan ke main.py yg mana akan lanjut cek validitas form sebelum menjalankan request method POST yang menambahkan form yang telah diisi sebagai produk sebelum mengembalikan user ke main
5. method show_products() di views.py akan mengambil id yang tertera dipanggil dalam URL request dan kemudian render show_products.html, mengisi field data dengan field data product yang uuid nya dipanggil. ada juga tombol 'back' yang memanggil url main untuk kembali ke main view

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    gk ada, alhamdulillah dapet 100

## foto
show_xml()
![alt text](image.png)

show_xml_by_id()
![alt text](image-1.png)

show_json()
![alt text](image-2.png)

show_json_by_id()
![alt text](image-3.png)

---

# Tugas 3

### **Penting: aku ga lupa naro last login, cuman aku style biar dia muncul di footer**

## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
authentication form adalah form bawaan django yang berguna untuk membanfingkan input username dan password dengan instansi user yang tertera di database dan juga memastikan akun user aktif(tidak di-disable)
### kelebihan:
- merupakan built in function
- terintegrasi dengan sistem user dan backend django
- memiliki keamanan standar(CSRF token, password hashing, etc)
### kekurangan
- tidak fleksibel
- perlu subclassing untuk kostumisasi logic dan UI
- tidak cocok untuk logic complex

## 2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
autentikasi adalah proses memverifikasi identitas user sedangkan otorisasi adalah proses memberi izin atau hak akses user.

### autentikasi:
- menggunakan django.contrib.auth, seperti authenticate(), login(), logout()
- membandingkan data(username dan password) input untuk mengambil instance user tersebut dari database
### otorisasi:
- menggunakan decorators(e.g @loginrequired) atau user function(user.has_perm())
- cek variable seperti: is_staff, is_authenticated atau variable permission costume untuk determine akses view

## 3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
### cookies:
#### kelebihan:
- disimpan di browser client, sehingga tidak perlu memori di server
- mudah diakses oleh client side
#### kekurangan:
- rawan manipulasi
- tidak terintegrasi sebaik session
- rentan data leak
### session:
#### kelebihan:
- disimpan di server, sehingga tidak mudah diakses dan lebih secure
- terintegrasi dengan API django
#### kekurangan:
- perlu memori di server
- tidak stateless sehingga beban memori bertambah setiap request

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
### Tidak
- bisa diakses dari client side
- http section bisa di-intercept dengan session hijacking
### Metode pengamanan django
- HttpOnly:true, sehingga cookies tidak bisa diakses lewat JS
- Secure:true, sehingga request hanya bisa via https
- SESSION_COOKIE_AGE, untuk batas waktu cookies bisa di kostumisasi
- CSRF, django generate CSRF token untuk menjaga dari serang CSRF

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. ### implementasi fungsi registrasi, login, logout:
    - import UserCreationForm, messages, AuthenticationForm, authenticate, login, logout, reverse, login_required, UserCreationForm dan AuthenticationForm dari library django
    - menambahkan fungsi register yang melakukan POST request dengan UserCreationForm built in django untuk menambah user ke database
    - menambah fungsi login yang melakukan POST request dengan AuthenticationForm built in.
        - username dan password user dibandingkan dengan database untuk cek apakah user ada di data base
        - instance user yang sesuai diambil dari database
        - fungsi membuka session untuk client
    - menambah fungsi logout yang terminate session dengan fungsi bawaan reverse dari django
    - menggunakan template login dan register yang disediakan di tutorial untuk laman login dan register
    - import fungsi .views ke .urls dan menghubungkan laman dan fungsi di url path
    - menambah decorator login_required ke main_view() dan show_products()
2. ###  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
    - register dua akun
    - add 3 product ke masing-masing akun
3. ###  Menghubungkan model Product dengan User.
    - import User dari django ke model
    - menambahkan parameter user, null=True digunakan agar model yang sebelumnya tidak memiliki user tidak corrupt
    - melakukan makemigrations dan migrate models
    - mengganti fungsi main_view di views untuk memasukan request.user sebagai parameter user
4. ### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
    - menambahkan request.COOKIES.get('last_login','never') ke main_view() lalu memasukkanya ke context dan kemudian menampilkan data di footer main.html
    - menambahkan request.user ke main_view() yang di-pass ke context lalu menampilkan username user di main.view
    - mmenambahkan if statements ke main.html untuk menunjukkan nama user atau anonymous untuk menunjukkan nama vendor di product cards di main.html dan show_products.html
    - membuat if statements di fungsi main_view() untuk filter products apa yang di load(product user atau semua product) ke list products di context. filter bisa diganti dari dropdown form yang ada di main.html

---

# Tugas 4

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas (specificity) dimulai dari deklarasi yang diberi `!important`, diikuti inline style (`style="..."`), selector dengan ID, selector kelas/atribut/pseudo-class, lalu selector elemen dan pseudo-elemen. Jika tingkat specificity sama, aturan yang muncul paling akhir di stylesheet yang sama yang dipakai.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memastikan tampilan nyaman di berbagai ukuran layar sehingga UX konsisten dan aksesibilitas meningkat. Misalnya, halaman utama Tokopedia sudah responsif: grid produk berubah dari banyak kolom di desktop menjadi satu kolom di ponsel sehingga mudah dinavigasi. Sebaliknya, beberapa portal akademik lama seperti SIAKAD versi klasik tidak responsif karena layout fix-width yang memaksa pengguna mobile melakukan zoom manual, menyebabkan interaksi sulit dan potensi salah input tinggi.

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang di luar kotak elemen untuk memberi jarak antar elemen; border adalah garis yang mengelilingi kotak elemen; padding adalah ruang antara konten dan border. Implementasinya dengan properti CSS `margin`, `border`, dan `padding`, misalnya:
```css
.card {
    margin: 1rem;
    border: 1px solid #cbd5f5;
    padding: 1.5rem;
}
```
Properti tersebut juga bisa menggunakan notasi shorthand (top-right-bottom-left) atau bernilai spesifik per sisi (`margin-top`, `padding-inline`, dan sebagainya).

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox adalah modul layout satu dimensi untuk menyusun elemen secara horizontal *atau* vertikal dengan mudah (align, justify, order). Cocok untuk bar navigasi, card list, atau mendistribusikan ruang di dalam satu baris/kolom. 
- Grid layout adalah modul dua dimensi yang memungkinkan kontrol baris dan kolom sekaligus, cocok untuk dashboard atau galeri karena setiap cell dapat diatur ukurannya dan posisinya secara eksplisit. Keduanya sering dikombinasikan: grid untuk kerangka besar, flexbox untuk isi tiap cell.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambahkan view `edit_product()` dan `delete_products()` di `main/views.py` untuk menangani pembaruan serta penghapusan entri. Kedua view dihubungkan lewat `main/urls.py` dan dibatasi `login_required` dan juga dengan product.user =  request.user supaya hanya pemilik produk yang bisa mengubah data.

2. Mengaktifkan Tailwind CDN di `templates/base.html` dan menulis stylesheet kustom `static/css/global.css` untuk komponen formulir. Kelas `form-style` dipakai di halaman login, register, tambah, dan edit produk (`main/templates/login.html`, `main/templates/register.html`, `main/templates/create_products.html`, `main/templates/edit_products.html`) agar input, checkbox, dan validasi tampil konsisten.

3. mengedit halaman daftar dan kartu produk (`main/templates/main.html`, `main/templates/card_products.html`) menjadi layout responsif. Jika belum ada data, template menampilkan ilustrasi `static/image/no_products.png` dan pesan kosong; bila ada data, tiap kartu memuat gambar/placeholder, vendor, harga, dan ringkasan deskripsi dengan grid adaptif.

4. Menambahkan tombol edit dan delete langsung di setiap kartu pada `main/templates/card_products.html`, dengan kondisi render `product.user == user` supaya hanya pemilik yang melihat aksinya.

5. Membangun navbar responsif di `templates/navbar.html` menggunakan flexbox untuk desktop dan menu hamburger untuk mobile. Script kecil men-toggle kelas `hidden` sehingga navigasi dan tombol login/register tetap dapat diakses di berbagai ukuran layar.

---

# Tugas 6

## 1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request memblokir alur execution sampai response diterima. Pada web tradisional, ini berarti halaman penuh direfresh untuk setiap aksi. Asynchronous request (AJAX/fetch) berjalan di latar tanpa memblokir UI. halaman tidak perlu reload, dan kita bisa memperbarui sebagian DOM saat respons datang. sehingga synchronous terasa lambat dan “patah”, sementara asynchronous terasa responsif karena interaksi dan render bisa berjalan bersamaan.

## 2. Bagaimana AJAX bekerja di Django (alur request–response)?
Ringkasnya:
- Client menjalankan `fetch()`/XHR dengan URL Django (mis. `path('json/', show_json, ...)`).
- Django URL resolver (urls.py) memetakan ke view (views.py).
- View memproses request (validasi, DB query) dan mengembalikan JSON/HTTP 2xx/4xx (sering via `JsonResponse`).
- Client menerima respons, lalu JS memperbarui DOM (mis. render list produk, menutup modal, menampilkan toast) tanpa reload halaman.
- Untuk form, kita kirim `FormData` + CSRF token; Django memverifikasi CSRF dan kredensial (untuk auth) sebelum menulis data.

## 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
- Interaksi lebih cepat: tidak ada full page reload, hanya data yang berubah yang dikirim/diterima.
- UX lebih baik: loading/empty/error state bisa ditangani inline dengan animasi/feedback langsung.
- Hemat bandwidth: payload umumnya JSON kecil, bukan HTML penuh.
- Komposabilitas: endpoint JSON yang sama bisa dipakai banyak komponen/halaman.
- Kontrol UI granular: kita bisa refresh sebagian kecil UI (e.g satu kartu produk) tanpa menyentuh bagian lain.

## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
- CSRF protection: sertakan `X-CSRFToken`/`csrfmiddlewaretoken` pada request POST; pastikan `CsrfViewMiddleware` aktif.
- Sanitasi input: gunakan form Django (UserCreationForm/AuthenticationForm) dan/atau `strip_tags` untuk field teks bebas; validasi di server tetap wajib.
- HTTPS: aktifkan `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` agar kredensial tidak bocor.
- Session & auth bawaan: gunakan `login()`/`logout()` dan middleware session Django; jangan bikin token auth custom tanpa kebutuhan.
- Batasi informasi error: kirim pesan error generik (hindari mengungkap apakah username ada/tidak), dan rate-limit bila perlu.

## 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
- Responsif: aksi terasa instan karena tidak perlu muat ulang halaman.
- Konsistensi konteks: state UI (scroll, filter, modal) tidak hilang tiap aksi.
- Feedback jelas: loading spinner, empty/error state, dan toast memberi kepastian status aksi.
- Aksesibilitas lebih baik: bila diimplementasikan dengan tepat (fokus, ARIA live regions), pembaca layar juga memperoleh feedback yang benar.
- Perceived performance meningkat: meski total kerja sama, transisi mikro yang mulus membuat aplikasi terasa lebih cepat.
