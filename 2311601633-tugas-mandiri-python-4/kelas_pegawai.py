# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Superclass
class Pegawai:
    def __init__(self, id_number, nama, telepon, departemen):
        self.id_number = id_number
        self.nama = nama
        self.telepon = telepon
        self.departemen = departemen

    def tampil_info(self):
        return f"ID: {self.id_number}, Nama: {self.nama}, Telepon: {self.telepon}, Departemen: {self.departemen}"


# Subclass untuk Pegawai Tetap
class PegawaiTetap(Pegawai):
    def __init__(self, id_number, nama, telepon, departemen, gaji_pokok, uang_makan, uang_transport):
        super().__init__(id_number, nama, telepon, departemen)
        self.gaji_pokok = gaji_pokok
        self.uang_makan = uang_makan
        self.uang_transport = uang_transport

    def tampil_gaji(self):
        total_gaji = self.gaji_pokok + self.uang_makan + self.uang_transport
        return f"Total Gaji: {total_gaji}"


# Subclass untuk Pegawai Honorer
class PegawaiHonorer(Pegawai):
    def __init__(self, id_number, nama, telepon, departemen, honor):
        super().__init__(id_number, nama, telepon, departemen)
        self.honor = honor

    def tampil_incentif(self):
        return f"Incentif: {self.honor}"


# Daftar pegawai
pegawai_list = [
    PegawaiTetap("001", "Jution", "08123456789", "IT", 5000000, 1000000, 500000),
    PegawaiHonorer("002", "Destry", "08198765432", "Tax Accounting", 3000000),
]

# Menampilkan informasi pegawai
for pegawai in pegawai_list:
    print(pegawai.tampil_info())
    if isinstance(pegawai, PegawaiTetap):
        print(pegawai.tampil_gaji())
    elif isinstance(pegawai, PegawaiHonorer):
        print(pegawai.tampil_incentif())
    print("-" * 40)
