# Praktik 1: Validasi dan Klasifikasi Nilai Akhir
# Input : nilai ujian, nilai tugas, kehadiran (persen) -> semua 0-100
# Proses: validasi tipe -> validasi rentang -> syarat kehadiran -> predikat -> status
# Output: nilai akhir (2 desimal), predikat, status kelulusan

print("Validasi dan Klasifikasi Nilai Akhir")

teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")

        if hadir < 80:
            print("Status: Tidak memenuhi syarat kehadiran.")
        else:
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 70:
                predikat = "B"
            elif akhir >= 60:
                predikat = "C"
            elif akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"

            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"

            print(f"Predikat: {predikat}")
            print(f"Status: {status}")

# ================= TEST CASE WAJIB =================
# Ujian | Tugas | Hadir | Nilai Akhir | Hasil yang diharapkan
#   90  |  80   |  95   |   86.00     | Predikat A, Lulus
#   75  |  70   |  85   |   73.00     | Predikat B, Lulus
#   60  |  60   |  80   |   60.00     | Predikat C, Lulus
#   55  |  50   |  90   |   53.00     | Predikat D, Belum lulus
#   40  |  30   | 100   |   36.00     | Predikat E, Belum lulus
#   90  |  90   |  75   |   90.00     | Nilai akhir tampil, Tidak memenuhi syarat kehadiran
#  105  |  80   |  90   |     -       | Pesan penolakan rentang nilai ujian
#   80  |  -5   |  90   |     -       | Pesan penolakan rentang nilai tugas
#   80  |  80   | abc   |     -       | Pesan penolakan tipe
