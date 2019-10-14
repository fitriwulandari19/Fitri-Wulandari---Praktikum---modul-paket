import hitung

def main():
    print("PENJUMLAHAN")
    bil1 = float(input("Masukkan bilangan 1: "))
    bil2 = float(input("Masukkan bilangan 2: "))

    hasil = hitung.tambah(bil1, bil2)
    
    print("Hasil: ", hasil)

if __name__ == "__main__":
    main()
