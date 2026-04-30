def insertion_sort(nama, stok):
    for i in range(1, len(stok)):
        temp_stok = stok[i]
        temp_nama = nama[i]
        j = i - 1
        while j >= 0 and stok[j] > temp_stok:
            stok[j + 1] = stok[j]
            nama[j + 1] = nama[j]
            j -= 1
        stok[j + 1] = temp_stok
        nama[j + 1] = temp_nama

def main():
    try:
        n = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Input tidak valid")
        return
    nama_barang = []
    stok_barang = []
    print("Masukkan data barang:")
    for i in range(n):
        nama = input(f"Nama barang ke {i+1}: ")
        while True:
            try:
                stok = int(input(f"Stok {nama}: "))
                if stok < 0:
                    print("Stok tidak boleh negatif")
                else:
                    break
            except ValueError:
                print("Input tidak valid")
        nama_barang.append(nama)
        stok_barang.append(stok)

    print("\nStok sebelum diurutkan:")
    for i in range(n):
        print(nama_barang[i], "=", stok_barang[i])

    insertion_sort(nama_barang, stok_barang)

    print("\nStok setelah diurutkan:")
    for i in range(n):
        print(nama_barang[i], "=", stok_barang[i])

if __name__ == "__main__":
    main()