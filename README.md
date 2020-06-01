# pikobar-covid-update
Cek berapa jumlah ODP,PDF dan Positif aktif saat ini di kelurahan kita, menggunakan API Publik Pikobar.

Cara menggunakan : 

1. Buka https://covid19-public.digitalservice.id/api/v1/sebaran_app/jabar?stage=Proses&kode_kab=3275 , sesuaikan kode_kab dengan kode kota/kabupaten kamu. Untuk mengetahui kode tersebut, download file .xls di sini https://pikobar.jabarprov.go.id/table-case/ . Setelah dibuka, akan muncul plaintext JSON. Copy seluruh isi teks JSON itu, masukkan kedalam file data.json
2. Buka line ke-17 file cov.py, ubah dengan nama kelurahan yang ingin kamu cari. Daftar nama kelurahan bisa dilihat di dalam file JSON yang tadi
3. Jalankan program cov.py

