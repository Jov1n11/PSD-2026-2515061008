# Program Pemutar Musik Menggunakan Doubly Linked List

# Deskripsi Singkat
Program ini merupakan program pemutar musik sederhana menggunakan double linked list, yang dapat digunakan untuk menambah musik, melihat riwayat atau daftar musik, serta berpindah ke musik sebelumnya dan berikutnya. Program dapat menampilkan playlist musik dan menandai musik yang sedang diputar. Double linked list digunakan karena setiap node dapat menggunakan dua pointer next untuk musik selanjutnya dan prev untuk musik sebelumnya. Struktur ini sangat cocok digunakan karena memungkinkan navigasi dua arah secara tanpa perlu mengulang dari awal.

# Source Code
<img width="271" height="116" alt="image" src="https://github.com/user-attachments/assets/c6fee0f8-cb40-4452-bd98-0acd8639948b" />
Pada baris 1–5, kode digunakan untuk membuat class Node yang berfungsi sebagai tempat menyimpan data musik. Pada baris 2 dibuat konstruktor __init__ yang akan dijalankan saat objek dibuat. Baris 3 menyimpan nama musik ke dalam atribut self.musik, sedangkan baris 4 dan 5 digunakan untuk menyimpan pointer ke node sebelumnya (prev) dan node berikutnya (next).  

<img width="260" height="94" alt="image" src="https://github.com/user-attachments/assets/7945c824-3378-4ce3-a278-9964adf94873" />
Pada baris 7–10, baris 7 dibuat class Riwayatmusik sebagai class utama untuk mengelola playlist. Baris 8 konstruktor, baris 9 self.head sebagai node pertama, dan baris 10 self.current sebagai penunjuk musik yang sedang diputar.  

<img width="400" height="264" alt="image" src="https://github.com/user-attachments/assets/62e750cd-c447-4d08-bdea-b00c0a450666" />
Pada baris 12–24, baris 12 didefinisikan fungsi tambah_musik yang digunakan untuk menambahkan musik ke dalam playlist. Baris 13 membuat node baru. Baris 14 mengecek apakah playlist masih kosong. Jika kosong (baris 15–16), maka node baru dijadikan head sekaligus current. Jika tidak kosong (baris 17–23), maka program mencari node terakhir menggunakan perulangan (baris 19–20), lalu menghubungkan node baru ke akhir list (baris 21–22). Baris 23 mengatur agar musik terbaru menjadi musik aktif. Baris 24 menampilkan output bahwa musik berhasil ditambahkan.   

<img width="380" height="266" alt="image" src="https://github.com/user-attachments/assets/e67d2ae4-f39a-4f3b-a20e-0b3b6808fc33" />
Pada baris 26–38, baris 26 didefinisikan fungsi playlist yang berfungsi menampilkan seluruh musik. Baris 27–29 mengecek apakah playlist kosong, jika iya maka program output "Belum ada musik". Baris 30 output "Daftar Musik". Baris 31 memulai dari node pertama, lalu baris 32–37 melakukan perulangan untuk menampilkan semua musik. Jika musik tersebut merupakan yang sedang aktif (baris 33–34), maka output diberi tanda panah (->), jika tidak maka output biasa (baris 35–36). Baris 37 digunakan untuk berpindah ke node berikutnya, dan baris 38 menambahkan enter agar tampilan lebih rapi.  

<img width="420" height="264" alt="image" src="https://github.com/user-attachments/assets/d05959c7-7684-433f-aa71-dd9d72d56c7f" />
Pada baris 40–45, baris 40 didefinisikan fungsi sebelumnya yang berfungsi untuk berpindah ke musik sebelumnya. Baris 41 mengecek apakah ada musik aktif dan memiliki node sebelumnya. Jika ada (baris 42-43), maka musik pindah ke musik sebelumnya (baris 43). Jika tidak ada (baris 44–45), maka output "tidak ada musik sebelumnya."  

<img width="431" height="132" alt="image" src="https://github.com/user-attachments/assets/809a01c0-3694-474a-8a02-77ce88f36810" />
Pada baris 47–52, baris 47 didefinisikan fungsi berikutnya yang berfungsi untuk berpindah ke musik berikutnya. Baris 48 mengecek apakah ada musik aktif dan memiliki node berikutnya. Jika ada (baris 49-50), maka musik pindah ke musik berikutnya (baris 50). Jika tidak ada (baris 51–52), maka output "tidak ada musik berikutnya."  

<img width="237" height="39" alt="image" src="https://github.com/user-attachments/assets/ecc098de-dc2b-40fd-9e21-fd24152bd0a8" />
Pada baris 54, dibuat objek riwayat dari class Riwayatmusik untuk digunakan dalam program utama.  

<img width="304" height="151" alt="image" src="https://github.com/user-attachments/assets/1910504e-cb87-4909-a49a-a90be63ddc96" />
Pada baris 56–62, merupakan program utama dengan perulangan while True agar program terus berjalan. Baris 57–62 menampilkan menu pilihan.  

<img width="402" height="285" alt="image" src="https://github.com/user-attachments/assets/fe6f7e0f-fbc4-419c-b945-38d1369fcf10" />
Baris 64 menerima input dari user. Baris 65–67 digunakan untuk menambahkan musik ke dalam playlist. Baris 68–69 menampilkan playlist. Baris 70–71 digunakan untuk berpindah ke musik sebelumnya. Baris 72–73 untuk berpindah ke musik berikutnya. Baris 74–76 digunakan untuk keluar dari program dengan cara menghentikan perulangan (break). Sedangkan baris 77–78 berfungsi jika input tidak valid.  

# Output Program
<img width="205" height="464" alt="image" src="https://github.com/user-attachments/assets/cb8e5a65-7dbc-4e8a-8ef0-3017e5f70c86" />
User memilih menu 1 (Tambah musik) sebanyak tiga kali, program meminta input nama musik, dan user menginput Musik1, Musik2, dan Musik3, setiap input berhasil disimpan dan output: "Musik 'Musik1/2/3' ditambahkan".  

<img width="148" height="190" alt="image" src="https://github.com/user-attachments/assets/759a98b4-c70e-4c44-a270-ba0a76125432" />
Saat memilih menu 2 (Lihat Playlist), program output:
Daftar musik
  Musik1
  Musik2
->Musik3
Tanda -> menunjukkan bahwa Musik3 adalah musik yang sedang aktif (current).  

<img width="194" height="323" alt="image" src="https://github.com/user-attachments/assets/960ba1ab-1ec2-4c01-9129-2fa2a8f26b9d" />
Saat memilih menu 3 (Musik Sebelumnya), program output: "Pindah ke musik sebelumnya"
Setelah itu, saat playlist ditampilkan kembali (menu 2):
  Musik1
->Musik2
  Musik3
Ini menunjukkan bahwa pointer telah berpindah ke node sebelumnya.  

<img width="197" height="322" alt="image" src="https://github.com/user-attachments/assets/d7ca3fb9-3165-4602-b7e2-e85b33c58b85" />
Saat memilih menu 4 (Musik Berikutnya), program output: "Pindah ke musik berikutnya"
Setelah itu, saat playlist ditampilkan kembali (menu 2):
  Musik1
  Musik2
->Musik3
Ini menunjukkan bahwa pointer telah berpindah ke node berikutnya.  

<img width="145" height="133" alt="image" src="https://github.com/user-attachments/assets/ad0bbf22-b443-4085-8144-abe00d0723c7" />
Saat user memasukkan angka selain 1-5, program output: "Pilihan tidak valid"  

<img width="141" height="133" alt="image" src="https://github.com/user-attachments/assets/68d4bb50-fa99-446a-b332-e19fed39c4b3" />
Saat pengguna memilih menu 5 (Keluar), program menampilkan: "Program selesai", kemudian program berhenti karena perintah break menghentikan perulangan while.  

# Link YouTube
https://youtu.be/ntBmf_wXR_I
