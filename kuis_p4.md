# Jawaban Kuis Formatif Pertemuan 4

**1. Apa arti kata `elif` dan kapan sebuah `elif` dievaluasi?**  
`elif` adalah singkatan dari *else if*. Sebuah cabang `elif` hanya dievaluasi ketika seluruh kondisi `if` atau `elif` di atasnya bernilai `False`.

---

**2. Mengapa rantai `if-elif-else` hanya menghasilkan satu keluaran?**  
Karena Python memeriksa kondisi dari atas ke bawah dan langsung berhenti saat menemukan kondisi pertama yang bernilai `True`. Setelah blok perintah dari cabang `True` tersebut selesai dijalankan, seluruh cabang sisanya akan dilewati.

---

**3. Apa yang terjadi jika rantai `elif` tidak ditutup dengan `else` dan tidak ada kondisi yang bernilai `True`?**  
Program tidak akan mengeksekusi blok aksi mana pun di dalam rantai tersebut, sehingga tidak ada keluaran yang ditampilkan (masukan melewati struktur seleksi tanpa hasil).

---

**4. Untuk aturan A mulai 85, B mulai 70, dan C mulai 60, mengapa kondisi harus disusun menurun?**  
Karena jika disusun menaik (misal `>= 60` terlebih dahulu), nilai tinggi seperti `90` akan memicu kondisi pertama menjadi `True` dan secara keliru dikategorikan sebagai C, sehingga kondisi untuk A dan B di bawahnya tidak pernah diperiksa.

---

**5. Tuliskan kondisi Python yang menyatakan nilai berada pada rentang 0 sampai 100 termasuk kedua ujungnya.**  
Format kondisi: `0 <= nilai <= 100`  
*(Atau menggunakan ekspresi logika: `nilai >= 0 and nilai <= 100`)*

---

**6. Sebutkan tiga jenis validasi input dan satu contoh masukan yang ditolak oleh masing-masing.**  
1. **Validasi Tipe:** Memeriksa apakah teks dapat dikonversi ke angka. *Contoh ditolak:* `"sembilan"` atau `"12a"`.
2. **Validasi Rentang:** Memeriksa apakah nilai berada pada interval yang sah. *Contoh ditolak:* `-5` atau `105` pada nilai skala 0–100.
3. **Validasi Domain:** Memeriksa apakah nilai termasuk pilihan yang dikenal. *Contoh ditolak:* `"biru"` untuk pilihan jawaban `"ya"`/`"tidak"`.

---

**7. Kesalahan apa yang ditangkap oleh `except ValueError` pada pemanggilan `float(teks)`?**  
`ValueError` ditangkap saat pemanggilan `float()` menerima string/teks yang tidak bisa dikonversi menjadi angka desimal (misalnya huruf atau teks kosong).

---

**8. Mengapa metode `isdigit()` tidak cocok untuk memvalidasi nilai bertipe desimal?**  
Karena metode `isdigit()` hanya mengembalikan `True` jika seluruh karakter terdiri dari angka bulat positif. Karakter titik desimal (`.`) atau tanda minus (`-`) dianggap bukan angka sehingga masukan desimal seperti `4.5` atau bilangan negatif `-3` akan menghasilkan `False` (ditolak).

---

**9. Apa gunanya memanggil `.strip().lower()` sebelum membandingkan jawaban ya atau tidak?**  
`.strip()` berguna untuk menghapus spasi di awal/akhir teks, sedangkan `.lower()` mengubah huruf menjadi kecil semua. Penggabungan keduanya membuat program toleran dan menganggap variasi input seperti `" Ya "`, `"YA"`, dan `"ya"` sebagai nilai yang sama.

---

**10. Sebutkan enam test case yang diperlukan untuk menguji program predikat nilai secara memadai.**  
1. **Nilai normal di setiap cabang:** Nilai `92` (A), `76` (B), `65` (C), `55` (D), `30` (E).
2. **Nilai tepat di titik batas:** Nilai `85`, `70`, `60`, `50`.
3. **Nilai tepat di sekitar batas:** Nilai `84.9`, `69.9`, `59.9`, `49.9`.
4. **Ujung rentang sah:** Nilai `0` dan `100`.
5. **Nilai di luar rentang sah:** Nilai `-1` dan `100.1`.
6. **Masukan bukan angka:** Teks `"abc"` atau teks kosong.