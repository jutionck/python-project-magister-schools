# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Soal 5
# Buatlah program menggunakan Bahasa Python untuk menghitung total tagihan parkir dengan
# terdiri dari komponen berikut ini :
# • Biaya parkir per jam (misalkan : Rp. 1.000,-)
# • Jam Masuk (misalkan : 08:00)
# • Jam Keluar (misalkan : 10:30)
# • Total menit dihitung menggunakan rumus = (jam keluar dikali dengan 60 ditambah menit
# keluar) - (jam masuk dikali dengan 60 ditambah menit masuk)
# • Lama parkir dihitung dengan rumus = Total menit dibagi dengan 60
# • Total tagihan parkir dihitung dengan rumus = lama parkir * biaya parkir
# Kemudian cetaklah total menit, lama parkir dan total tagihan parkir untuk setiap kendaraan.

# Input data dari pengguna
biaya_per_jam = int(input("Masukkan biaya parkir per jam (Rp): "))
jam_masuk = input("Masukkan jam masuk (HH:MM): ")
jam_keluar = input("Masukkan jam keluar (HH:MM): ")

# Memisahkan jam dan menit dari input
jm, mm = map(int, jam_masuk.split(":"))
jk, mk = map(int, jam_keluar.split(":"))

# Menghitung total menit dari waktu masuk dan keluar
total_masuk = jm * 60 + mm
total_keluar = jk * 60 + mk

# Menghitung total menit parkir
total_menit = total_keluar - total_masuk

# Menghitung lama parkir dalam jam
lama_parkir = total_menit // 60  # Jam penuh
sisa_menit = total_menit % 60    # Sisa menit

# Jika ada sisa menit, tambahkan 1 jam ke tagihan
if sisa_menit > 0:
    lama_parkir += 1

# Menghitung total tagihan parkir
total_tagihan = lama_parkir * biaya_per_jam

# Menampilkan hasil
print("\nHasil:")
print(f"Total Menit Parkir: {total_menit} menit")
print(f"Lama Parkir: {lama_parkir} jam")
print(f"Total Tagihan Parkir: Rp {total_tagihan:,}")