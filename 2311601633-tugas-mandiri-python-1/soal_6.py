# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 6
# Buatlah program menggunakan Bahasa Python untuk menghitung total angsuran per bulan dengan
# terdiri dari komponen berikut ini :
# • Jumlah pinjaman dalam satuan Rupiah.
# • Lama pinjaman dalam satuan bulan.
# • Bunga pinjaman dalam satuan Rupiah.
# • Biaya administrasi dalam satuan Rupiah
# • Jumlah angsuran dihitung dengan rumus = jumlah pinjaman dikalikan dengan bunga pinjaman
# • Jumlah bunga dihitung dengan rumus = 8% dikalikan dengan jumlah pinjaman
# • Total angsuran dihitung dengan rumus = jumlah angsuran ditambah dengan jumlah bunga
# Kemudian cetaklah jumlah pinjaman, lama pinjaman dan total angsuran yang dibayarkan.

# Input data dari pengguna
jumlah_pinjaman = float(input("Masukkan jumlah pinjaman (Rp): "))
lama_pinjaman = int(input("Masukkan lama pinjaman (bulan): "))
bunga_pinjaman = float(input("Masukkan bunga pinjaman (%): "))
biaya_administrasi = float(input("Masukkan biaya administrasi (Rp): "))

# Menghitung jumlah bunga
jumlah_bunga = (bunga_pinjaman / 100) * jumlah_pinjaman

# Menghitung jumlah angsuran pokok
jumlah_angsuran_pokok = jumlah_pinjaman / lama_pinjaman

# Menghitung total angsuran per bulan
total_angsuran_per_bulan = jumlah_angsuran_pokok + (jumlah_bunga / lama_pinjaman) + (biaya_administrasi / lama_pinjaman)

# Menghitung total angsuran selama masa pinjaman
total_angsuran = total_angsuran_per_bulan * lama_pinjaman

# Menampilkan hasil
print("\nHasil perhitungan angsuran:")
print(f"Jumlah Pinjaman: Rp {jumlah_pinjaman:,.2f}")
print(f"Lama Pinjaman: {lama_pinjaman} bulan")
print(f"Total Angsuran per Bulan: Rp {total_angsuran_per_bulan:,.2f}")
print(f"Total Angsuran Selama Masa Pinjaman: Rp {total_angsuran:,.2f}")
