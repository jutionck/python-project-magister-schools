# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 1
# Buatlah program menggunakan Bahasa Python untuk mencetak pasangan nilai X dan nilai Y,
# dimana hubungan antara X dan Y memenuhi persamaan Y = X2 – 2X + 1. 
# Kemudian cetaklah nilai X dan nilai Y tersebut.

# Input rentang nilai X
start = int(input("Masukkan nilai awal X: "))
end = int(input("Masukkan nilai akhir X: "))

# Menampilkan header tabel
print("\nPasangan nilai X dan Y:")
print("X\tY")

# Menghitung dan mencetak pasangan nilai X dan Y
for x in range(start, end + 1):
    y = x**2 - 2*x + 1
    print(f"{x}\t{y}")
