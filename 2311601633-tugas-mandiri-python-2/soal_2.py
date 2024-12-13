# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains


# Buatlah program untuk menghitung harga layanan yang dikenakan kepada member dengan ketentuan sbb:
# Input:
# kode member, nama member, biaya layanan, lama menjadi member.
# Proses:
# masing-masing member akan diberikan diskon berdasarkan lama bergabung menjadi member. Diskon ditentukan sebagai berikut :
# Lama member lebih besar atau sama dengan 20 tahun, diberikan diskon 15% dari biaya layanan.
# Lama member lebih besar atau sama dengan 10 tahun, diberikan diskon 10% dari biaya layanan.
# Lama member lebih besar atau sama dengan 5 tahun, diberikan diskon 5% dari biaya layanan.
# Lama member kurang dari 5 tahun, tidak diberikan diskon.
# Output:
# kode member, nama member, biaya layanan, lama menjadi member, diskon

def hitung_diskon(biaya, lama):
    if lama >= 20:
        diskon = 0.15
    elif lama >= 10:
        diskon = 0.10
    elif lama >= 5:
        diskon = 0.05
    else:
        diskon = 0.0
    return diskon, biaya * diskon

def main():
    print("+" + "="*42 + "+")
    print("| NIM: 2311601633                          |")
    print("| Nama: Jution Candra Kirana               |")
    print("| Program Menghitung Harga Layanan Member  |")
    print("+" + "="*42 + "+")

    kode_member = input("Kode Member    : ").strip()
    nama_member = input("Nama           : ").strip()
    biaya_layanan = float(input("Biaya Layanan  : "))
    lama_member = int(input("Lama (Tahun)   : "))

    persen_diskon, jumlah_diskon = hitung_diskon(biaya_layanan, lama_member)
    total_biaya = biaya_layanan - jumlah_diskon

    print("\n" + "=" * 40)
    print(f"Kode Member    : {kode_member}")
    print(f"Nama           : {nama_member}")
    print(f"Biaya Layanan  : {biaya_layanan}")
    print(f"Lama (Tahun)   : {lama_member}")
    print(f"Diskon         : {persen_diskon * 100:.0f}%")
    print(f"Potongan Diskon: {jumlah_diskon:.1f}")
    print(f"Total Biaya    : {total_biaya:.1f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
