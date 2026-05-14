# Program Sistem Antrian Kasir Menggunakan Queue Linked List

# Deskripsi Singkat
Program ini merupakan simulasi sistem antrian kasir minimarket yang dibuat menggunakan struktur data Queue Linked List. Program digunakan untuk mengatur urutan pelanggan yang datang dan dilayani berdasarkan prinsip FIFO (First In First Out), yaitu pelanggan yang datang lebih dulu akan dilayani lebih dulu. Struktur data yang digunakan adalah Queue Linked List. Queue dipilih karena sangat cocok digunakan pada sistem antrian di dunia nyata seperti kasir, rumah sakit, bank, dan layanan customer service. Linked List digunakan agar ukuran antrian dapat bertambah secara dinamis tanpa batas ukuran pada array.

# Source Code
<img width="268" height="97" alt="Screenshot 2026-05-14 143830" src="https://github.com/user-attachments/assets/d893f149-032b-4378-9d38-0b4b29b3628a" />

Pada baris 1–4, baris 1 didefinisikan class Node yang digunakan untuk menyimpan data pelanggan pada antrian. Pada baris 2, dibuat constructor __init__() yang menerima parameter nama. Pada baris 3, data nama pelanggan disimpan ke dalam atribut self.nama. Pada baris 4, atribut self.next diisi None yang berfungsi sebagai penunjuk ke node berikutnya pada Linked List.

<img width="254" height="95" alt="image" src="https://github.com/user-attachments/assets/8327991e-cd09-49a3-a860-d5a23e17c4ce" />

Pada baris 6–9, baris 6 didefinisikan class QueueKasir yang digunakan sebagai struktur utama queue. Pada baris 7 dibuat constructor __init__(). Pada baris 8–9, dibuat variabel front dan rear dengan nilai awal None yang digunakan untuk menunjuk bagian depan dan belakang antrian.

<img width="307" height="53" alt="image" src="https://github.com/user-attachments/assets/f1bfbf85-a888-4fa6-b16b-b72745c6c9c5" />

Pada baris 11–12, baris 11 didefinisikan fungsi is_empty() untuk mengecek apakah queue kosong atau tidak. Jika front bernilai None, maka fungsi akan mengembalikan nilai True.

<img width="413" height="191" alt="image" src="https://github.com/user-attachments/assets/30707940-80f8-4baf-9c8b-75731050dcfa" />

Pada baris 14–22, baris 14 didefinisikan fungsi ambil_antrian() yang digunakan untuk menambahkan pelanggan ke dalam antrian. Pada baris 15, dibuat node baru menggunakan Node(nama). Pada baris 16 dilakukan pengecekan apakah queue kosong menggunakan is_empty(). Pada baris 17–18, jika queue kosong maka front dan rear akan menunjuk ke node baru. Pada baris 19–21, jika queue tidak kosong maka node baru ditambahkan di belakang queue menggunakan rear.next, lalu rear dipindahkan ke node baru. Pada baris 22, program menampilkan pesan bahwa pelanggan berhasil masuk antrian.

<img width="475" height="190" alt="image" src="https://github.com/user-attachments/assets/2d7a38e5-f5e4-43d2-97fd-ba9f2562bf8e" />

Pada baris 24–32, baris 24 didefinisikan fungsi layani_pelanggan() yang digunakan untuk melayani pelanggan paling depan pada queue. Pada baris 25 dilakukan pengecekan apakah queue kosong. Pada baris 26–27, jika queue kosong maka program akan menampilkan pesan “Tidak ada pelanggan dalam antrian” lalu fungsi berhenti menggunakan return. Pada baris 28, data pelanggan paling depan disimpan ke variabel pelanggan. Pada baris 29, program menampilkan pelanggan yang sedang dilayani. Pada baris 30, pointer front dipindahkan ke node berikutnya sehingga pelanggan paling depan terhapus dari queue. Pada baris 31–32, jika setelah penghapusan queue menjadi kosong maka rear diubah menjadi None.

<img width="394" height="225" alt="image" src="https://github.com/user-attachments/assets/9c4ef49b-520a-460b-8bdb-6d164dbfdab8" />

Pada baris 34–44, baris 34 didefinisikan fungsi lihat_antrian() yang digunakan untuk menampilkan seluruh isi antrian. Pada baris 35 dilakukan pengecekan apakah queue kosong. Pada baris 36–37, jika queue kosong maka program output pesan “Antrian kosong”. Pada baris 38, program output "Daftar antrian". Pada baris 39, current diisi front untuk memulai pencarian dalam Linked List. Pada baris 40, dibuat variabel nomor untuk penomoran antrian. Pada baris 41–44 dilakukan perulangan while untuk menampilkan seluruh data pelanggan dari depan ke belakang hingga current bernilai None.

<img width="459" height="417" alt="image" src="https://github.com/user-attachments/assets/17984e4d-6c76-40a9-af29-4eb829d95704" />

Pada baris 46–66, baris 46 didefinisikan fungsi main() sebagai program utama. Pada baris 47 dibuat objek kasir dari class QueueKasir. Pada baris 48 digunakan perulangan while True agar menu terus berjalan sampai user memilih keluar program. Pada baris 49–53, program menampilkan menu utama sistem antrian kasir. Pada baris 54, user diminta menginputkan pilihan. Pada baris 55–57, jika user input "1" maka program meminta nama pelanggan lalu memanggil fungsi ambil_antrian(). Pada baris 58–59, jika user input "2" maka program memanggil fungsi layani_pelanggan(). Pada baris 60–61, jika user input "3" maka program memanggil fungsi lihat_antrian(). Pada baris 62–64, jika user input "4" maka program output pesan “Program selesai” lalu menghentikan program menggunakan break. Pada baris 65–66, jika input bukan 1-4 maka program output pesan “Pilihan tidak valid”.

<img width="244" height="39" alt="image" src="https://github.com/user-attachments/assets/0a7b25e7-9975-4b23-b0a1-bd7aa4da334d" />

Pada baris 68-69, program dijalankan menggunakan if __name__ == "__main__": untuk memastikan fungsi main() yang dieksekusi.

# Output Program
<img width="219" height="289" alt="image" src="https://github.com/user-attachments/assets/2532209d-46f9-4436-8dfd-7271e034a6a8" />

User input "1" dua kali untuk mengambil antrian, lalu program meminta nama pelanggan, kemudian user memasukkan nama "Budi" dan "Udin".

<img width="164" height="160" alt="image" src="https://github.com/user-attachments/assets/9abd8427-15af-4579-bbd3-fa4afd033e20" />

User input "3", lalu program menampilkan isi queue dari depan ke belakang sesuai urutan kedatangan pelanggan.

<img width="221" height="121" alt="image" src="https://github.com/user-attachments/assets/b09295e4-48e1-4bee-866e-470e9f3f25ef" />

User input "2", lalu program melayani Budi karena prinsip queue yaitu melayani pelanggan dari depan ke belakang sesuai urutan kedatangan pelanggan.

<img width="144" height="133" alt="image" src="https://github.com/user-attachments/assets/2ad4f8d4-2cf4-4096-aa5b-f28f99d00b24" />

User input "3" lagi, lalu program menampilkan sisa isi queue yaitu "Udin".


<img width="149" height="123" alt="image" src="https://github.com/user-attachments/assets/53d353a0-27d4-4c86-97ac-029f23a5f658" />

User input "5", lalu program output pesan “Pilihan tidak valid” karena "5" bukan salah satu pilihan menu pada program.

<img width="147" height="119" alt="image" src="https://github.com/user-attachments/assets/f8b75e36-780f-42d5-9111-1a45e602b844" />

User input "4", lalu program berhenti.

# Link YouTube
https://youtu.be/r4L-_nYc_Kc
