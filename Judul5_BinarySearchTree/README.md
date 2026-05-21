# Program Pendataan Barang di Toko Buku Menggunakan Binary Search Tree

# Deskripsi Singkat
Program ini merupakan sistem pendataan barang toko sederhana yang dibuat menggunakan struktur data Binary Search Tree. Program dapat digunakan untuk menambahkan data barang, mencari barang berdasarkan ID, dan menampilkan seluruh data barang secara terurut berdasarkan ID barang. Struktur data Binary Search Tree digunakan karena mampu melakukan proses pencarian, penambahan, dan pengurutan data dengan cepat dibanding list biasa. Pada program ini setiap node menyimpan ID barang dan nama barang. Data barang dengan ID lebih kecil disimpan di sebelah kiri node, sedangkan data dengan ID lebih besar disimpan di sebelah kanan node.

# Source Code
<img width="354" height="133" alt="image" src="https://github.com/user-attachments/assets/31c21aa3-9501-4feb-b27c-4ac1b6b4f0fc" />

Pada baris 1–6, dibuat class Node yang digunakan untuk menyimpan data barang. Pada baris 2 dibuat constructor. Pada baris 3–4 data disimpan ke dalam object. Pada baris 5–6 dibuat pointer left dan right.

<img width="240" height="76" alt="image" src="https://github.com/user-attachments/assets/00991e4d-7d65-4bac-8db8-9a3d9ebe4570" />

Pada baris 8–10, dibuat class BST sebagai struktur utama. Pada baris 9 dibuat constructor. Pada baris 10 ada root dengan nilai awal None.

<img width="595" height="169" alt="image" src="https://github.com/user-attachments/assets/56c883cf-968b-417e-a196-c0cf3af4407c" />

Pada baris 12–19, dibuat fungsi insert_node() untuk menambahkan data barang ke BST. Pada baris 13 dilakukan pengecekan apakah root kosong. Jika kosong maka dibuat node baru. Pada baris 15–16, jika id_barang lebih kecil dari root maka data dimasukkan ke subtree kiri. Pada baris 17–18, jika id_barang lebih besar maka data dimasukkan ke subtree kanan.

<img width="545" height="57" alt="image" src="https://github.com/user-attachments/assets/70491416-dd88-4644-84b4-ea7221b13460" />

Pada baris 21–22, dibuat fungsi insert() untuk memanggil fungsi insert_node().

<img width="488" height="170" alt="image" src="https://github.com/user-attachments/assets/119fe9aa-6283-42a9-9b15-5be034e7a6d8" />

Pada baris 24–31, dibuat fungsi search_node() untuk mencari data barang berdasarkan ID barang. Pada baris 25–26 dilakukan pengecekan apakah node kosong. Pada baris 27–28, jika ID barang merupakan root maka output akan root. Pada baris 29–30, jika ID lebih kecil maka pencarian dilakukan ke subtree kiri. Jika lebih besar maka pencarian dilakukan ke subtree kanan.

<img width="462" height="56" alt="image" src="https://github.com/user-attachments/assets/d5cda605-9e94-4553-bf05-7d9ab43049f7" />

Pada baris 33–34, dibuat fungsi search() untuk memanggil fungsi search_node().

<img width="390" height="171" alt="image" src="https://github.com/user-attachments/assets/18b15118-b265-47f0-89d3-26d78e390ab2" />

Pada baris 36–43, didefinisikan fungsi inorder() untuk menampilkan seluruh data barang secara terurut.

<img width="530" height="778" alt="image" src="https://github.com/user-attachments/assets/c353345e-0275-4f88-9d93-af246adb9954" />

Pada baris 45–84, dibuat fungsi main() sebagai program utama.
Pada baris 46 dibuat object bst. Pada baris 49–52 program menampilkan menu utama. Pada baris 54–57 dilakukan input pilihan menu.
Pada baris 59–66, jika user memilih menu 1 maka program meminta input ID barang dan nama barang lalu data dimasukkan ke BST menggunakan fungsi insert().
Pada baris 67–77, jika user memilih menu 2 maka program meminta input ID barang yang dicari lalu memanggil fungsi search(). Jika data ditemukan maka program menampilkan nama barang.
Pada baris 78–80, jika user memilih menu 3 maka program menampilkan seluruh data barang menggunakan inorder agar output berurutan dari ID barang terkecil ke terbesar.
Pada baris 81–82, jika user memilih menu 4 maka program berhenti dan output pesan “Program selesai.”

<img width="247" height="41" alt="image" src="https://github.com/user-attachments/assets/ca180f70-7f0b-4654-907f-5338ea85b3da" />

Pada baris 86–87, program dijalankan menggunakan if __name__ == "__main__": untuk memastikan fungsi main() yang dieksekusi.

# Output Program
<img width="248" height="676" alt="image" src="https://github.com/user-attachments/assets/42acb75c-2c6a-4b6d-ad35-cd41d0cd9b2f" />

User input "1" untuk menambahkan data barang. Program meminta input ID barang dan nama barang. User memasukkan ID barang 100 dengan nama barang Buku, kemudian program menampilkan pesan “Barang berhasil ditambahkan”. Setelah itu user memilih 1 lagi dan menambahkan ID 50 Pensil, ID 25 Pena, dan ID 150 Penggaris.

<img width="229" height="337" alt="image" src="https://github.com/user-attachments/assets/bb1784c2-9de5-4840-8bbc-19e134529202" />

User input "3", untuk menampilkan seluruh data barang. Program menampilkan daftar barang menggunakan traversal inorder sehingga data tampil secara terurut berdasarkan ID barang yaitu 25, 50, 100, dan 150.

<img width="249" height="320" alt="image" src="https://github.com/user-attachments/assets/88cc13ae-7806-44ba-b91b-a39ae22ec84f" />

User input "2", untuk mencari data barang berdasarkan ID barang. User mencari ID 100 dan program berhasil menemukan ID 100 dengan nama barang “Buku”. Setelah itu user mencari ID 125, namun program menampilkan pesan “Barang tidak ditemukan” karena data tersebut tidak ada di dalam BST.

<img width="223" height="122" alt="image" src="https://github.com/user-attachments/assets/d67992ff-4a8a-41e4-81ad-4c3a272c893c" />

User input "5", lalu program output pesan “Pilihan tidak valid” karena "5" bukan salah satu pilihan menu pada program.

<img width="209" height="122" alt="image" src="https://github.com/user-attachments/assets/6934e8bc-0393-44a9-baac-78d03505a9f4" />

User input "4", lalu program berhenti.

# Link YouTube
https://youtu.be/MNno1wccX2Y
