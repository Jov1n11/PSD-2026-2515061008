# Program Pencarian Kontak Menggunakan Binary Search

# Deskripsi Singkat
Program ini merupakan program pencarian kontak sederhana yang menggunakan Binary Search, yang dapat digunakan untuk mencari data kontak berdasarkan nama. Program menyimpan data berupa nama dan nomor telepon, kemudian user dapat memasukkan nama yang ingin dicari. Jika ditemukan, program akan output nama beserta nomor telepon. Binary Search digunakan karena proses pencarian data menjadi lebih cepat dibandingkan pencarian biasa. Metode ini bekerja dengan cara membagi data menjadi dua bagian berulang hingga data ditemukan. Binary Search cocok digunakan pada data yang sudah terurut seperti daftar kontak karena dapat mencari data dengan cepat.

# Source Code
<img width="412" height="303" alt="image" src="https://github.com/user-attachments/assets/1d7c3b00-63e0-493c-8d48-9bfc11d78059" />
Pada baris 1–15, baris 1 didefinisikan fungsi binary_search_kontak yang digunakan untuk mencari data nama dalam daftar kontak menggunakan Binary Search. Pada baris 2–3, ditentukan batas pencarian yaitu indeks awal (kiri = 0) dan indeks akhir (kanan = len(kontak) - 1). Pada baris 4, input diubah menjadi huruf kecil menggunakan lower() agar pencarian dapat tetap dilakukan walau user input dalam huruf kapital ataupun huruf kecil. Pada baris 5, dilakukan proses pencarian menggunakan perulangan while. Baris 6-8 menentukan tengah. Pada baris 9–14 dilakukan perbandingan, jika data sama dengan target, maka fungsi mengembalikan data kontak dari input, jika data lebih kecil, pencarian dilanjutkan ke kanan, jika data lebih besar, pencarian dilanjutkan ke kiri. Pada baris 15, jika data tidak ditemukan, fungsi akan mengembalikan nilai -1.

<img width="494" height="402" alt="image" src="https://github.com/user-attachments/assets/62c8eb69-c539-4f00-ba0c-db0b8f7e353b" />
Pada baris 17-36, baris 17 didefinisikan fungsi main() sebagai program utama. Pada baris 18-26, dibuat data kontak dalam bentuk list berisi nama dan nomor telepon. Pada baris 27-29, program akan output daftar nama kontak kepada user. Pada baris 30-31, user diminta memasukkan nama yang ingin dicari. Pada baris 31, program memanggil fungsi binary_search_kontak untuk melakukan pencarian. Pada baris 32-36 dilakukan pengecekan hasil, jika data ditemukan (index != -1), maka program output nama beserta nomor telepon "(Nama) ditemukan dengan nomor (...)", jika tidak ditemukan, program output pesan "Nama tidak ditemukan".

<img width="248" height="40" alt="image" src="https://github.com/user-attachments/assets/e05ba313-ee15-4be5-ac1c-7d5cb5e60499" />
Pada baris 38-39, program dijalankan menggunakan if __name__ == "__main__": untuk memastikan fungsi main() yang dieksekusi.

# Output Program
<img width="284" height="219" alt="image" src="https://github.com/user-attachments/assets/dc69e30c-8232-4ff6-b975-2173aece3d3a" />
Output 1: Program output daftar nama beserta nomor telepon kepada user lalu meminta user untuk memasukkan nama yang ingin dicari, lalu user memasukkan nama "Dina". Setelah itu, program output melakukan proses Binary Search dan output: "Mengecek: Dina". Karena data cocok dengan target pencarian, program berhasil menemukan nama dan output nomor telepon yang sesuai.

<img width="286" height="238" alt="image" src="https://github.com/user-attachments/assets/a1b5f971-2627-47d1-94fb-44164760ed59" />
Output 2: Sama seperti output 1, program akan output daftar nama beserta nomor telepon kepada user lalu meminta user untuk memasukkan nama yang ingin dicari, tetapi user memasukkan nama "budi". Karena ada fungsi lower(), program tetap melakukan proses Binary Search dan output: "Mengecek: Dina" "Mengecek: Budi". Program berhasil menemukan nama tersebut dan output nomor telepon yang sesuai.

<img width="275" height="222" alt="image" src="https://github.com/user-attachments/assets/fb0752b9-e1df-4a85-861e-631a3084a413" />
Output 3: Begitu juga dengan output 3, program tetap akan melakukan proses Binary Search walaupun seluruh input dari user menggunakan huruf kapital pada input "CITRA".

<img width="269" height="257" alt="image" src="https://github.com/user-attachments/assets/b97e415e-0438-42f2-956c-29562a2e9dd4" />
Output 4: Pada output 4, user memasukkan nama “Udin”, program melakukan proses pencarian hingga data habis diperiksa, namun karena nama tersebut tidak ada pada daftar kontak, program akhirnya output pesan "Nama tidak ditemukan".

# Link YouTube
https://youtu.be/WWjXTlsIpoE
