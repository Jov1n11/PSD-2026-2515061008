class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class QueueKasir:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None

    def ambil_antrian(self, nama):
        new_node = Node(nama)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{nama} berhasil masuk antrian")

    def layani_pelanggan(self):
        if self.is_empty():
            print("Tidak ada pelanggan dalam antrian")
            return
        pelanggan = self.front.nama
        print(f"Pelanggan {pelanggan} sedang dilayani")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def lihat_antrian(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Daftar antrian:")
        current = self.front
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.nama}")
            current = current.next
            nomor += 1

def main():
    kasir = QueueKasir()
    while True:
        print("\nSISTEM ANTRIAN KASIR")
        print("1. Ambil Antrian")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar Program")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            nama = input("Masukkan nama pelanggan: ")
            kasir.ambil_antrian(nama)
        elif pilihan == "2":
            kasir.layani_pelanggan()
        elif pilihan == "3":
            kasir.lihat_antrian()
        elif pilihan == "4":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()