# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 4
# Buatlah program menggunakan Bahasa Python untuk menghitung gaji bersih pegawai dengan
# terdiri dari komponen berikut ini :
# • Gaji pokok dalam satuan Rupiah
# • Uang transport dalam satuan Rupiah
# • Jumlah kehadiran dalam satuan hari
# • Pajak dalam satuan Rupiah
# • Total Transport dihitung dengan rumus = uang transport x jumlah hari
# • Total gaji dihitung dengan rumus = gaji pokok + total transport
# • Pajak dihitung dengan rumus = 10% dikali dengan total gaji
# • Gaji bersih dihitung dengan rumus = gaji pokok – pajak
# Kemudian cetaklah total gaji, pajak dan gaji bersih yang diperoleh pegawai.

# Input data dari pengguna
gaji_pokok = float(input("Masukkan gaji pokok (Rp): "))
uang_transport = float(input("Masukkan uang transport per hari (Rp): "))
jumlah_kehadiran = int(input("Masukkan jumlah hari kehadiran: "))

# Menghitung total transport
total_transport = uang_transport * jumlah_kehadiran

# Menghitung total gaji
total_gaji = gaji_pokok + total_transport

# Menghitung pajak
pajak = 0.1 * total_gaji

# Menghitung gaji bersih
gaji_bersih = total_gaji - pajak

# Menampilkan hasil
print("\nHasil:")
print(f"Total Gaji: Rp {total_gaji:,.2f}")
print(f"Pajak: Rp {pajak:,.2f}")
print(f"Gaji Bersih: Rp {gaji_bersih:,.2f}")
