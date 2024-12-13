# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 2
# Buatlah program menggunakan Bahasa Python untuk menghitung jumlah energi kinetik sebuah
# benda (dalam satuan Joule), dimana energi kinetik dapat dihitung dengan rumus EK = ½ x m x V2
# • EK = energi kinetik dalam satuan J (Joule).
# • M = masa jenis dalam satuan Kg (kilogram).
# • V = kecepatan benda dalam satuan m/s (meter/second)
# Kemudian cetaklah nilai EK, nilai m dan nilai v tersebut.


# Input nilai massa (m) dan kecepatan (v)
m = float(input("Masukkan massa benda (kg): "))
v = float(input("Masukkan kecepatan benda (m/s): "))

# Menghitung energi kinetik
EK = 0.5 * m * v**2

# Menampilkan hasil
print("\nHasil:")
print(f"Massa (m): {m} kg")
print(f"Kecepatan (v): {v} m/s")
print(f"Energi Kinetik (EK): {EK:.2f} Joule")
