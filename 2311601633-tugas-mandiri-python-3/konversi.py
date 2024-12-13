# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Buat script Python menggunakan User-Defined Function untuk:
# - menginputkan sejumlah data (NIM, Nama, Nilai Tugas, UTS dan UAS)
# - hitung nilai akhir dengan formula: nilai akhir = 30% tugas + 30% uts + 40% uas
# - konversi nilai akhir menjadi Grade, dengan formula:

#  85-100      A 
# 80- <85      A-
#  75- <80      B+
#  70- <75      B
#  65- <70      B-
#  60- <65      C
#  45- <60      D
#  0- <45      E
# - hitung total nilai
# - hitung rata-rata nilai
# - cari nilai tertinggi beserta NIM dan Nama
# - cari nilai terendah beserta NIM dan Nama

# Function minimal yang harus ada adalah:

# hitung nilai akhir
# konversi grade
# cetak hasil

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

def konversi_grade(nilai_akhir):
    if 85 <= nilai_akhir <= 100:
        return "A"
    elif 80 <= nilai_akhir < 85:
        return "A-"
    elif 75 <= nilai_akhir < 80:
        return "B+"
    elif 70 <= nilai_akhir < 75:
        return "B"
    elif 65 <= nilai_akhir < 70:
        return "B-"
    elif 60 <= nilai_akhir < 65:
        return "C"
    elif 45 <= nilai_akhir < 60:
        return "D"
    elif 0 <= nilai_akhir < 45:
        return "E"
    else:
        return "T"  # Nilai tidak valid

def cetak_hasil(data_mahasiswa):
    total_nilai = sum([m["nilai_akhir"] for m in data_mahasiswa])
    rata_rata = total_nilai / len(data_mahasiswa)
    tertinggi = max(data_mahasiswa, key=lambda x: x["nilai_akhir"])
    terendah = min(data_mahasiswa, key=lambda x: x["nilai_akhir"])

    print("\nLaporan Nilai Data Science")
    print("+" + "="*65 + "+")
    print(f"| {'No.':<3} | {'NIM':<10} | {'Nama':<10} | {'TGS':<3} | {'UTS':<3} | {'UAS':<3} | {'Akhir':<5} | {'Grade':<5} |")
    print("+" + "="*65 + "+")
    for i, m in enumerate(data_mahasiswa):
        print(f"| {i+1:<3} | {m['nim']:<10} | {m['nama']:<10} | {int(m['tugas']):<3} | {int(m['uts']):<3} | {int(m['uas']):<3} | {m['nilai_akhir']:<5.2f} | {m['grade']:<5} |")
    print("+" + "="*65 + "+")

    print(f"Total Nilai    : {total_nilai:.2f}")
    print(f"Nilai Rata-rata: {rata_rata:.2f}")
    print(f"Nilai Tertinggi: {tertinggi['nilai_akhir']:.2f}, NIM: {tertinggi['nim']} - Nama: {tertinggi['nama']}")
    print(f"Nilai Terendah : {terendah['nilai_akhir']:.2f}, NIM: {terendah['nim']} - Nama: {terendah['nama']}")

def main():
    print("Program Pengolahan Nilai Mahasiswa\n")
    
    jumlah_mahasiswa = int(input("Jumlah Mahasiswa: "))
    data_mahasiswa = []

    for i in range(jumlah_mahasiswa):
        print(f"\nInputkan Data ke-{i+1}")
        nim = input("NIM       : ")
        nama = input("Nama      : ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS  : "))
        uas = float(input("Nilai UAS  : "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        grade = konversi_grade(nilai_akhir)
        data_mahasiswa.append({
            "nim": nim,
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir,
            "grade": grade
        })

    cetak_hasil(data_mahasiswa)

if __name__ == "__main__":
    main()
