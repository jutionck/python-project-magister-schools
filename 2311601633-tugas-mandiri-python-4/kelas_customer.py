# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Superclass
class Customer:
    def __init__(self, id_number, nama, alamat, telepon):
        self.id_number = id_number
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon

    def tampil_profil(self):
        return f"ID: {self.id_number}, Nama: {self.nama}, Alamat: {self.alamat}, Telepon: {self.telepon}"


# Subclass untuk Member
class Member(Customer):
    def __init__(self, id_number, nama, alamat, telepon, hrg_member, diskon):
        super().__init__(id_number, nama, alamat, telepon)
        self.hrg_member = hrg_member
        self.diskon = diskon

    def tampil_biaya(self):
        total_biaya = self.hrg_member - self.diskon
        return f"Total Biaya (Member): {total_biaya}"


# Subclass untuk NonMember
class NonMember(Customer):
    def __init__(self, id_number, nama, alamat, telepon, hrg_nonmember):
        super().__init__(id_number, nama, alamat, telepon)
        self.hrg_nonmember = hrg_nonmember

    def tampil_biaya(self):
        return f"Total Biaya (NonMember): {self.hrg_nonmember}"


# Daftar customer
customer_list = [
    Member("001", "Jution", "Jl. Musyawarah Jakarta Selatan", "08123456789", 500000, 50000),
    NonMember("002", "Destry", "Jl. Musyawarah Jakarta Selatan", "08198765432", 300000),
]

# Menampilkan informasi customer
for customer in customer_list:
    print(customer.tampil_profil())
    print(customer.tampil_biaya())
    print("-" * 40)
