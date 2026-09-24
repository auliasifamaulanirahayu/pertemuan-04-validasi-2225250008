# Latihan 2: Kategori Bilangan
# Input : satu bilangan bulat
# Aturan: negatif | nol | positif genap | positif ganjil
# Output: kategori bilangan

x = int(input("Masukkan bilangan bulat: "))

if x < 0:
    print("Bilangan negatif")
elif x == 0:
    print("Nol")
elif x % 2 == 0:
    print("Bilangan positif genap")
else:
    print("Bilangan positif ganjil")

# Test case:
# -7 -> Bilangan negatif
# 0  -> Nol
# 8  -> Bilangan positif genap
# 13 -> Bilangan positif ganjil
