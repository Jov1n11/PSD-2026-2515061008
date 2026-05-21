class Node:
    def __init__(self, id_barang, nama):
        self.id_barang = id_barang
        self.nama = nama
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, id_barang, nama):
        if root is None:
            return Node(id_barang, nama)
        if id_barang < root.id_barang:
            root.left = self.insert_node(root.left, id_barang, nama)
        elif id_barang > root.id_barang:
            root.right = self.insert_node(root.right, id_barang, nama)
        return root

    def insert(self, id_barang, nama):
        self.root = self.insert_node(self.root, id_barang, nama)

    def search_node(self, root, id_barang):
        if root is None:
            return None
        if root.id_barang == id_barang:
            return root
        if id_barang < root.id_barang:
            return self.search_node(root.left, id_barang)
        return self.search_node(root.right, id_barang)

    def search(self, id_barang):
        return self.search_node(self.root, id_barang)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print("ID Barang :", root.id_barang)
        print("Nama Barang :", root.nama)
        print()
        self.inorder(root.right)

def main():
    bst = BST()
    pilih = 0
    while pilih != 4:
        print("\n=== DATA BARANG TOKO BUKU ===")
        print("1. Tambah Barang")
        print("2. Cari Barang")
        print("3. Tampilkan Barang")
        print("4. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                id_barang = int(input("Masukkan ID Barang: "))
                nama = input("Masukkan Nama Barang: ")
                bst.insert(id_barang, nama)
                print("Barang berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                id_barang = int(input("Cari ID Barang: "))
                hasil = bst.search(id_barang)
                if hasil:
                    print("Barang ditemukan")
                    print("Nama Barang :", hasil.nama)
                else:
                    print("Barang tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("\nDaftar Barang:")
            bst.inorder(bst.root)
        elif pilih == 4:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
    