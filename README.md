# Unfollow-back-Instagram-script

# Deskripsi

Skrip ini digunakan untuk membandingkan daftar followers dan following di Instagram, lalu menghasilkan file HTML yang berisi akun yang Anda ikuti, tetapi tidak mengikuti Anda kembali. Data followers dan following diambil dari file JSON yang diunduh secara manual dari pengaturan akun Instagram.

# Persyaratan

1. **Termux**: Aplikasi terminal emulator untuk Android.
2. **Python 3**: Versi Python yang diperlukan untuk menjalankan skrip.
3. **Skrip Python**: File skrip [generate-report-follower-insta.py](https://github.com/BoyOs04/Unfollow-back-Instagram-script/blob/4fb9fc712c9b0e8cfe6c6eb6b10f21270e7bd2f3/generate-report-follower-insta.py) yang digunakan untuk menghasilkan laporan HTML.
## pakai script yang ini `generate-report-follower-insta.py`
# Langkah-langkah Instalasi

## 1. Install Termux

Unduh dan instal Termux dari Google Play Store atau F-Droid.

## 2. Install Python di Termux

Buka Termux dan jalankan perintah berikut untuk menginstal Python:

pkg update
pkg install python

## 3. Memberikan Akses Penyimpanan ke Termux

Untuk mengakses penyimpanan umum seperti /storage/emulated/0/, Anda harus memberikan izin akses penyimpanan ke Termux. Jalankan perintah berikut:

termux-setup-storage

Izinkan Termux mengakses penyimpanan eksternal saat diminta.

## 4. Pindahkan Skrip ke Penyimpanan Umum

#### 1. Buat folder baru di penyimpanan umum (misalnya di /storage/emulated/0/InstagramScript/):

mkdir /storage/emulated/0/InstagramScript


#### 2. Pindahkan skrip listnotfollow-html.py ke folder umum yang baru saja Anda buat:

mv listnotfollow-html.py /storage/emulated/0/InstagramScript/



# 5. Mengunduh Informasi Follower dan Following Secara Manual

## 1. Masuk ke Instagram melalui browser atau aplikasi.


## 2. Navigasi ke Pengaturan:

Pada aplikasi Instagram, klik pada ikon profil Anda di pojok kanan bawah.

Klik menu tiga garis di pojok kanan atas, lalu masuk ke Settings (Pengaturan).

## 3. Download Your Data:

Masuk ke menu Security (Keamanan), lalu pilih Download Data.

Instagram akan mengirimkan tautan untuk mengunduh semua data akun Anda, termasuk followers dan following.

Anda akan menerima email dengan tautan untuk mengunduh data dalam beberapa jam.

## 4. Ekstrak Data:

Data akan diunduh dalam bentuk file ZIP. Buka file ZIP tersebut di file manager Anda untuk melihat semua file data, termasuk daftar followers dan following.

Letakkan file followers_1.json dan following.json di dalam folder /storage/emulated/0/ig/f/.

# 6. Menjalankan Skrip

Setelah semua data JSON sudah ditempatkan di folder yang benar, jalankan skrip dengan perintah berikut di Termux:

python /storage/emulated/0/InstagramScript/listnotfollow-html.py

# 7. Hasil Output

Skrip ini akan menghasilkan file HTML bernama not_following_back.html yang berisi daftar akun yang tidak mengikuti Anda kembali. File ini akan disimpan di lokasi berikut:

/storage/emulated/0/ig/f/not_following_back.html

Anda dapat membuka file HTML ini dengan browser untuk melihat daftar akun yang Anda ikuti tetapi tidak mengikuti Anda kembali.

# 8. Bantuan

Jika Anda memerlukan bantuan lebih lanjut atau ingin bertanya sesuatu, silakan kunjungi [ChatGPT](https://chat.com) untuk bantuan tambahan.

Perhatikan tempat penyimpanan file / nama folder
