# E-commerce-Data-Analysis
# Nama Proyek
**Analisis Penjualan dengan Streamlit**

## Deskripsi
Proyek ini adalah aplikasi analisis penjualan yang dibuat dengan menggunakan Streamlit. Aplikasi ini memungkinkan pengguna untuk memvisualisasikan data penjualan, melihat tren penjualan bulanan, serta menampilkan produk terlaris berdasarkan total penjualan. Aplikasi ini menggunakan dataset yang terdiri dari informasi pesanan dan item pesanan.

## Fitur
- Visualisasi tren penjualan bulanan.
- Tabel interaktif untuk data gabungan pesanan dan item pesanan.
- Menampilkan jumlah data yang hilang di setiap kolom.
- Menampilkan 5 produk terlaris berdasarkan total penjualan.

## Prerequisites
Sebelum menjalankan aplikasi, pastikan Anda memiliki hal-hal berikut:
- Python 3.6 atau lebih baru
- pip (Python package installer)

## Instalasi
Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi ini:

1. Clone repositori ini ke mesin lokal Anda:
   ```bash
   git clone <URL_REPOSITORI>
   cd <NAMA_FOLDER_PROYEK>
2. Buat dan aktifkan environment virtual (opsional tapi disarankan):
    ```bash
   python -m venv env
   source env/bin/activate  # Untuk Mac/Linux
   .\env\Scripts\activate  # Untuk Windows

3. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt

## Menjalankan Aplikasi
- Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah berikut:
    ```bash
   streamlit run app.py

## Dataset
Dataset yang digunakan dalam aplikasi ini terdiri dari:

orders_dataset.csv: Berisi informasi tentang pesanan, termasuk tanggal dan total nilai pesanan.
order_items_dataset.csv: Berisi rincian tentang item dalam setiap pesanan.
Silakan unggah kedua file dataset ini saat diminta oleh aplikasi untuk melakukan analisis.

## Lisensi
Proyek ini dilisensikan di bawah [Nama Lisensi]. Lihat file LICENSE untuk lebih detail.

## Penulis
Amalina Shabrina
Email: [amalinashabrina2504@students.unnes.ac.id]


