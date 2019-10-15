import hitung

#tambah
def main():
    print("PENJUMLAHAN")
    bil1 = float(input("Masukkan bilangan 1: "))
    bil2 = float(input("Masukkan bilangan 2: "))

    hasil = hitung.tambah(bil1, bil2)
    
    print("Hasil: ", hasil)

#kurang
    print("-----------------------------------")
    print("PENGURANGAN")
    bil1 = float(input("Masukkan bilangan 1: "))
    bil2 = float(input("Masukkan bilangan 2: "))

    hasil = hitung.kurang(bil1, bil2)
    
    print("Hasil: ", hasil)

#kali
    print("-----------------------------------")
    print("PERKALIAN")
    bil1 = float(input("Masukkan bilangan 1: "))
    bil2 = float(input("Masukkan bilangan 2: "))

    hasil = hitung.kali(bil1, bil2)
    
    print("Hasil: ", hasil)

#bagi
    print("-----------------------------------")
    print("PEMBAGIAN")
    bil1 = float(input("Masukkan bilangan 1: "))
    bil2 = float(input("Masukkan bilangan 2: "))

    hasil = hitung.bagi(bil1, bil2)
    
    print("Hasil: ", hasil)


if __name__ == "__main__":
    main()
