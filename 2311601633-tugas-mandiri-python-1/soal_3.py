# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 3
# Buatlah program menggunakan Bahasa Python untuk menghitung total tagihan listrik dengan
# terdiri dari komponen berikut ini :
# • Tarif listrik per jam (misalkan : Rp. 1.457,-)
# • Jumlah KWH Awal (misalkan : 2500)
# • Jumlah KWH Akhir (misalkan : 2960)
# • Jumlah KWH terpakai dihitung dengan rumus = KWH Akhir dikurangi dengan KWH Awal.
# • Total tagihan listrik dihitung dengan rumus = jumlah KWH terpakai * tarif Listrik
# Kemudian cetaklah jumlah KWH terpakai dan total tagihan listrik yang diperoleh.

# Input data dari pengguna
tarif_per_jam = float(input("Masukkan tarif listrik per jam (Rp): "))
kwh_awal = int(input("Masukkan jumlah KWH awal: "))
kwh_akhir = int(input("Masukkan jumlah KWH akhir: "))

# Menghitung jumlah KWH terpakai
kwh_terpakai = kwh_akhir - kwh_awal

# Menghitung total tagihan listrik
total_tagihan = kwh_terpakai * tarif_per_jam

# Menampilkan hasil
print("\nHasil:")
print(f"Jumlah KWH Terpakai: {kwh_terpakai} KWH")
print(f"Total Tagihan Listrik: Rp {total_tagihan:,.2f}")
