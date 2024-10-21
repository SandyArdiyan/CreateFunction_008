#prak 3 no 2
import math

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r**2
# Input jari-jari
jari_jari = 5

# Menghitung luas
area = luas_lingkaran(jari_jari)

# Menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")