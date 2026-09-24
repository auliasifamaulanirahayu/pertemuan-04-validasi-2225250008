# Latihan 3: Validasi Rentang - Jenis Sudut
# Input : besar sudut (derajat), sah jika 0 < sudut < 180
# Output: jenis sudut atau pesan penolakan

sudut = float(input("Besar sudut dalam derajat: "))

if sudut <= 0 or sudut >= 180:
    print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
elif sudut < 90:
    print("Sudut lancip")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut tumpul")

# Test case:
# 45  -> Sudut lancip
# 90  -> Sudut siku-siku
# 135 -> Sudut tumpul
# 0   -> Pesan penolakan
# 180 -> Pesan penolakan
# -30 -> Pesan penolakan
