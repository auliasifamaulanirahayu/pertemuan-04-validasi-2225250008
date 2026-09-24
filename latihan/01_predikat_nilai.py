# Latihan 1: Predikat Nilai
# Input : nilai akhir (0-100)
# Aturan: >=85 A | 70-84.9 B | 60-69.9 C | 50-59.9 D | <50 E
# Output: predikat nilai

nilai = float(input("Nilai akhir (0-100): "))

if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")

# Test case:
# 92 -> A | 85 -> A | 84.9 -> B | 70 -> B | 60 -> C | 50 -> D | 49.9 -> E
