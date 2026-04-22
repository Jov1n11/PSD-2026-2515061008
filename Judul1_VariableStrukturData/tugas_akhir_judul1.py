class Node:
    def __init__(self, musik):
        self.musik = musik
        self.prev = None
        self.next = None

class Riwayatmusik:
    def __init__(self):
        self.head = None
        self.current = None

    def tambah_musik(self, musik):
        baru = Node(musik)
        if not self.head:
            self.head = baru
            self.current = baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = baru
            baru.prev = temp
            self.current = baru
        print(f"Musik '{musik}' ditambahkan")

    def playlist(self):
        if not self.current:
            print("Belum ada musik")
            return
        print("Daftar musik")
        temp = self.head
        while temp:
            if temp == self.current:
                print("->", temp.musik)
            else:
                print("  ", temp.musik)
            temp = temp.next
        print("\n")

    def sebelumnya(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print("Pindah ke musik sebelumnya")
        else:
            print("Tidak ada musik sebelumnya")

    def berikutnya(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("Pindah ke musik berikutnya")
        else:
            print("Tidak ada musik berikutnya")

riwayat = Riwayatmusik()

while True:
    print("====Menu====")
    print("1. Tambah musik")
    print("2. Lihat Playlist")
    print("3. Musik Sebelumnya")
    print("4. Musik Berikutnya")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        musik = input("Masukkan nama musik: ")
        riwayat.tambah_musik(musik)
    elif pilihan == "2":
        riwayat.playlist()
    elif pilihan == "3":
        riwayat.sebelumnya()
    elif pilihan == "4":
        riwayat.berikutnya()
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")