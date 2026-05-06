def binary_search_kontak(kontak, target):
    kiri = 0
    kanan = len(kontak) - 1
    target = target.lower()
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nama_tengah = kontak[tengah][0].lower()
        print(f"Mengecek: {kontak[tengah][0]}")
        if nama_tengah == target:
            return tengah
        elif nama_tengah < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

def main():
    kontak = [
        ("Andi", "081234567890"),
        ("Budi", "082345678901"),
        ("Citra", "083456789012"),
        ("Dina", "084567890123"),
        ("Eka", "085678901234"),
        ("Fajar", "086789012345"),
        ("Gina", "087890123456")
    ]
    print("Daftar kontak:")
    for nama, nomor in kontak:
        print(f"- {nama} : {nomor}")
    target = input("\nMasukkan nama yang ingin dicari: ")
    index = binary_search_kontak(kontak, target)
    if index != -1:
        nama, nomor = kontak[index]
        print(f"\n{nama} ditemukan dengan nomor {nomor}")
    else:
        print("\nNama tidak ditemukan")

if __name__ == "__main__":
    main()