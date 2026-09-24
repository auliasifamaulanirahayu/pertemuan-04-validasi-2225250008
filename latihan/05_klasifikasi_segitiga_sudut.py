# Latihan 5: Klasifikasi Segitiga Berdasarkan Sudut
# Input : tiga sudut segitiga (derajat)
# Syarat: semua sudut > 0 dan jumlah tepat 180 derajat
# Output: jenis segitiga (lancip/siku-siku/tumpul) berdasarkan sudut terbesar

a = float(input("Sudut A: "))
b = float(input("Sudut B: "))
c = float(input("Sudut C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
elif abs(a + b + c - 180) > 1e-9:
    print("Masukan ditolak: jumlah ketiga sudut harus 180 derajat.")
else:
    terbesar = max(a, b, c)
    if terbesar > 90:
        print("Segitiga tumpul")
    elif terbesar == 90:
        print("Segitiga siku-siku")
    else:
        print("Segitiga lancip")

# Test case:
# 60,60,60   -> Segitiga lancip
# 90,45,45   -> Segitiga siku-siku
# 120,30,30  -> Segitiga tumpul
# 100,50,40  -> Pesan penolakan jumlah sudut
# 0,90,90    -> Pesan penolakan sudut positif
