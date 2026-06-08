# Program Pencarian Data Mahasiswa Menggunakan HashMap Separate Chaining

# Deskripsi Singkat
Program ini merupakan sistem pencarian data mahasiswa sederhana yang dibuat menggunakan struktur data HashMap Separate Chaining. Program dapat digunakan untuk menyimpan data mahasiswa berdasarkan NPM dan mencari data mahasiswa berdasarkan NPM yang dimasukkan oleh pengguna. Setiap data mahasiswa terdiri dari NPM sebagai key dan nama mahasiswa sebagai value. Struktur data HashMap dipilih karena mampu melakukan proses pencarian data dengan cepat. Untuk menangani collision atau tabrakan data yang memiliki indeks hash yang sama, program menggunakan metode Separate Chaining, dengan metode ini, proses penyimpanan dan pencarian data tetap berjalan dengan baik meskipun terjadi collision.

# Source Code
<img width="310" height="117" alt="image" src="https://github.com/user-attachments/assets/4a8208e4-ec56-4071-9176-de3a6cdd6e02" />

Pada baris 1–5 dibuat class Node yang digunakan untuk menyimpan data mahasiswa. Pada baris 2 dibuat constructor. Pada baris 3 nilai key digunakan untuk menyimpan NPM. Pada baris 4 nilai value digunakan untuk menyimpan nama. Pada baris 5 dibuat pointer next yang digunakan untuk menghubungkan node satu dengan node lain dalam linked list.

<img width="352" height="93" alt="image" src="https://github.com/user-attachments/assets/83ed347d-4ef8-4eae-b46f-79b3c28c19ac" />

Pada baris 7–10 dibuat class HashMapNPM sebagai struktur utama HashMap. Pada baris 8 dibuat constructor. Pada baris 9 ukuran HashMap disimpan ke dalam variabel SIZE. Pada baris 10 dibuat array table sebanyak ukuran HashMap.

<img width="479" height="56" alt="image" src="https://github.com/user-attachments/assets/04270ed2-cdbd-441a-9ee2-059678923bef" />

Pada baris 12–13 dibuat fungsi hash_function() yang digunakan untuk menentukan indeks penyimpanan data. Fungsi ini menggunakan operasi modulo (%) untuk menghasilkan indeks bucket berdasarkan NPM.

<img width="380" height="225" alt="image" src="https://github.com/user-attachments/assets/a7cba56f-adb5-4099-84b7-7e6cb93de196" />

Pada baris 15–25 dibuat fungsi insert() yang digunakan untuk menambahkan data mahasiswa ke dalam HashMap. Pada baris 16 ditentukan indeks penyimpanan menggunakan fungsi hash. Pada baris 17 diambil node pertama pada bucket tersebut. Pada baris 18–22 dilakukan pengecekan apakah key sudah ada. Jika ditemukan, maka value diperbarui. Pada baris 23 dibuat node baru. Pada baris 24 node baru dihubungkan dengan node yang sudah ada pada bucket tersebut. Pada baris 25 node baru disimpan sebagai node pertama pada bucket.

<img width="348" height="169" alt="image" src="https://github.com/user-attachments/assets/46c33a06-1931-4a86-a334-3e7c30f5359d" />

Pada baris 27–34 dibuat fungsi search() yang digunakan untuk mencari data mahasiswa berdasarkan NPM. Pada baris 28 ditentukan bucket yang akan dicari menggunakan fungsi hash. Pada baris 29 diambil node pertama pada bucket tersebut. Pada baris 30–33 dilakukan traversal linked list hingga data ditemukan. Jika key ditemukan maka node dikembalikan. Jika tidak ditemukan maka fungsi mengembalikan nilai None.

<img width="591" height="190" alt="image" src="https://github.com/user-attachments/assets/24d3a424-e293-4e70-ac6c-41d38db3d45d" />

Pada baris 36–44 dibuat fungsi display() yang digunakan untuk menampilkan seluruh isi HashMap. Pada baris 37 ditampilkan judul data mahasiswa. Pada baris 38–43 dilakukan perulangan untuk menampilkan seluruh bucket dan isi linked list yang terdapat pada masing-masing bucket. Pada baris 44 ditampilkan tulisan NULL jika kosong.

<img width="330" height="208" alt="image" src="https://github.com/user-attachments/assets/a3e5727b-d686-478a-add9-83448205c405" />

Pada baris 46 dibuat fungsi main() sebagai program utama. Pada baris 47 dibuat objek HashMap bernama hashmap. Pada baris 48–54 dimasukkan data mahasiswa ke dalam HashMap menggunakan fungsi insert(). Pada baris 55 fungsi display() dipanggil untuk menampilkan seluruh data mahasiswa yang tersimpan pada HashMap.

<img width="453" height="152" alt="image" src="https://github.com/user-attachments/assets/c256b41a-8422-4670-bde4-1f0849f10a9a" />

Pada baris 57 program meminta pengguna memasukkan NPM yang ingin dicari. Pada baris 59-63 fungsi search() dipanggil untuk mencari data mahasiswa berdasarkan NPM yang dimasukkan pengguna, lalu dilakukan pengecekan hasil pencarian. Jika data ditemukan maka program menampilkan nama mahasiswa yang sesuai. Jika data tidak ditemukan maka program menampilkan pesan "Mahasiswa tidak ditemukan".

<img width="249" height="40" alt="image" src="https://github.com/user-attachments/assets/9094dac4-4a9e-4b20-ac64-1d04906c531f" />

Pada baris 65–66, program dijalankan menggunakan if name == "main": untuk memastikan fungsi main() yang dieksekusi.


# Output Program
<img width="337" height="236" alt="image" src="https://github.com/user-attachments/assets/d6f21cf9-2be6-46ff-a5e5-6ff1b61b5870" />

Program menampilkan seluruh data mahasiswa yang tersimpan pada HashMap. Selanjutnya user memasukkan NPM 2515001 pada kolom pencarian. Program melakukan pencarian dan berhasil menemukan data mahasiswa dengan nama Andi, kemudian menampilkan pesan "Mahasiswa ditemukan: Andi".

<img width="333" height="237" alt="image" src="https://github.com/user-attachments/assets/9f4a8f84-2edb-4b18-a221-b80c2cd302c4" />

Program menampilkan seluruh data mahasiswa yang tersimpan pada HashMap. Selanjutnya user memasukkan NPM 2515005 pada kolom pencarian. Karena NPM tersebut tidak ada dalam HashMap, program menampilkan pesan "Mahasiswa tidak ditemukan".

# Link YouTube
https://youtu.be/jys4iIGYIrY
