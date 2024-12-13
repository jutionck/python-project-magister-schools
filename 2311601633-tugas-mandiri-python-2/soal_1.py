# Tugas Mandiri
# NIM: 2311601633
# Nama: Jution Candra Kirana
# Mata Kuliah: Data Sains

# Buat program untuk menginput 3 (tiga) buah bilangan bulat, 
# (dianggap ketiga buah bilangan tersebut nilainya tidak sama satu dengan yanglain), 
# kemudian cetaklah bilangan yang nilainya merupakan nilai tengah ( bukan yang terbesar juga bukan yang terkecil).

def cari_nilai_tengah(a, b, c):
    angka = [a, b, c]
    angka.sort()
    return angka[1]

def main():
    print("+" + "="*37 + "+")
    print("| NIM: 2311601633                     |")
    print("| Nama: Jution Candra Kirana          |")
    print("| Program untuk mencetak nilai tengah |")
    print("| dari tiga buah nilai yang diinput   |")
    print("+" + "="*37 + "+")
    
    lanjut = 'y'
    while lanjut == 'y':
        print()
        input_angka = input("Input 3 Angka (pisahkan dengan spasi): ").strip()
        angka = input_angka.split()
        
        if len(angka) == 3:
            a = int(angka[0])
            b = int(angka[1])
            c = int(angka[2])
            
            if a == b or a == c or b == c:
                print("Error: Angka tidak boleh sama. Coba lagi.")
                continue
            
            print(f"Angka 1: {a}")
            print(f"Angka 2: {b}")
            print(f"Angka 3: {c}")
            
            nilai_tengah = cari_nilai_tengah(a, b, c)
            print(f"Nilai Tengah: {nilai_tengah}")
        else:
            print("Harap masukkan tepat 3 angka.")
        
        print()
        lanjut = input("Lanjut? (y/t): ").lower()
        if lanjut != 'y':
            print("Program selesai. Terima kasih!")
            break

if __name__ == "__main__":
    main()
