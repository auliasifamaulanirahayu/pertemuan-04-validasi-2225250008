# Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input

Nama: Aulia Sifa Maulani Rahayu
NIM: 2225250008
Kelas: A

## Tujuan
Membangun program validasi dan klasifikasi nilai akhir mahasiswa menggunakan
rantai `if-elif-else` serta validasi tipe, rentang, dan keterkaitan antardata
(kehadiran).

## Cara Menjalankan
```bash
python3 praktik/validasi_klasifikasi_nilai.py
```

## Tabel Keputusan

| Kategori | Syarat (setelah data valid & kehadiran >= 80%) | Contoh Masukan | Keluaran |
|---|---|---|---|
| A | nilai_akhir >= 85 | 90 | Predikat A |
| B | nilai_akhir >= 70 | 75 | Predikat B |
| C | nilai_akhir >= 60 | 60 | Predikat C |
| D | nilai_akhir >= 50 | 55 | Predikat D |
| E | selain di atas | 40 | Predikat E |

| Kondisi Penolakan | Syarat | Pesan |
|---|---|---|
| Tipe salah | salah satu input bukan angka | Masukan ditolak: seluruh data harus berupa angka. |
| Ujian di luar rentang | ujian < 0 atau ujian > 100 | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. |
| Tugas di luar rentang | tugas < 0 atau tugas > 100 | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. |
| Kehadiran di luar rentang | hadir < 0 atau hadir > 100 | Masukan ditolak: kehadiran di luar rentang 0 sampai 100. |
| Kehadiran kurang | hadir < 80 (setelah data valid) | Status: Tidak memenuhi syarat kehadiran. |

## Hasil Pengujian

| Ujian | Tugas | Hadir | Nilai Akhir Diharapkan | Keluaran Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|---|---|---|
| 90 | 80 | 95 | 86.00 | Predikat A, Lulus | 86.00, Predikat A, Lulus | Sesuai |
| 75 | 70 | 85 | 73.00 | Predikat B, Lulus | 73.00, Predikat B, Lulus | Sesuai |
| 60 | 60 | 80 | 60.00 | Predikat C, Lulus | 60.00, Predikat C, Lulus | Sesuai |
| 55 | 50 | 90 | 53.00 | Predikat D, Belum lulus | 53.00, Predikat D, Belum lulus | Sesuai |
| 40 | 30 | 100 | 36.00 | Predikat E, Belum lulus | 36.00, Predikat E, Belum lulus | Sesuai |
| 90 | 90 | 75 | 90.00 | Nilai akhir tampil, Tidak memenuhi syarat kehadiran | 90.00, Tidak memenuhi syarat kehadiran | Sesuai |
| 105 | 80 | 90 | - | Pesan penolakan rentang nilai ujian | Pesan penolakan rentang nilai ujian | Sesuai |
| 80 | -5 | 90 | - | Pesan penolakan rentang nilai tugas | Pesan penolakan rentang nilai tugas | Sesuai |
| 80 | 80 | abc | - | Pesan penolakan tipe | Pesan penolakan tipe | Sesuai |

## Refleksi
Masukan tidak valid yang semula mudah terlewat adalah kehadiran bertanda
negatif atau di atas 100 (misalnya diketik tanpa sengaja), karena fokus awal
sering hanya pada validasi nilai ujian dan tugas. Solusinya adalah menambahkan
elif khusus untuk memvalidasi rentang kehadiran sebelum memeriksa syarat
minimal 80 persen, sehingga ketiga data tetap diperiksa secara konsisten
sebelum masuk ke tahap klasifikasi.
