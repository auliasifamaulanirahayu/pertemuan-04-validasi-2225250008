# Latihan 4: Validasi Tipe - Ketuntasan Soal
# Input : jumlah soal benar dari 20 soal
# Output: persentase & keterangan tuntas/belum tuntas (batas 75%)

teks = input("Jumlah soal benar dari 20: ").strip()

try:
    benar = int(teks)
except ValueError:
    print("Masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("Masukan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = benar / 20 * 100
        print(f"Persentase = {persen:.2f} persen")
        if persen >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")

# Test case:
# 15 -> 75.00 persen, Tuntas
# 14 -> 70.00 persen, Belum tuntas
# 20 -> 100.00 persen, Tuntas
# 0  -> 0.00 persen, Belum tuntas
# 21 -> Pesan penolakan rentang
# "dua belas" -> Pesan penolakan tipe
