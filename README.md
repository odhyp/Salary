# ASIK

## Apa itu ASIK?

ASIK (Aplikasi Slip Gaji Elektronik) adalah sebuah aplikasi yang digunakan untuk mencetak Slip Gaji bulanan pegawai dalam bentuk _softfile_ yang kemudian dikirim ke pegawai yang bersangkutan melalui email.

---

## Modul Utama

1. Download CRViewer1 di SIPKD
2. Update data di database sekarang (sesuai dengan bulan Slip Gaji)
3. Formatting tampilan data di excel dan export ke PDF
4. Kirim lewat Whatsapp/email

---

## Fitur

1. Membuat Slip Gaji pegawai dalam bentuk PDF
2. Mengirim Slip Gaji ke setiap pegawai secara otomatis
3. Formatting CRViewer1.xlsx (Data Gaji)

---

## Breakdown Module

### Module 1 - _Browser Automation_

- Read username dan password di dalam password.txt
- Login ke SIPKD
- Navigasi ke daftar gaji PNS/Naban sesuai dengan bulan
- Download CRViewer.xls

### Module 2 - _Working with files_

- Pindahkan CRViewer.xls dari "Downloads" ke "asik/data"
- Convert dari .xls ke .xlsx
- Rename sesuai dengan Jenis Pegawai dan Bulan

### Module 3 - _Excel format & Export PDF_

- Memperbarui database gaji untuk PNS dan Naban
- Siapkan file excel untuk Slip Gaji
- Ubah isian sesuai dengan database
- Export ke PDF

### Module 4 - _Send files using email_

- Siapkan database untuk email pegawai
- Siapkan semua Slip Gaji terbaru dalam directory
- Siapkan format isi email
- Kirim Slip Gaji melalui email masing-masing pegawai