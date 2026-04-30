# Program Pengurutan Stok Barang Gudang Menggunakan Insertion Sort

# Deskripsi Singkat
Program ini merupakan program pengelolaan stok barang gudang sederhana yang menggunakan algoritma insertion sort, yang dapat digunakan untuk menambahkan data barang berupa nama dan jumlah stok, melihat daftar barang, serta mengurutkan stok dari yang terkecil ke terbesar. Program dapat menampilkan data sebelum dan sesudah proses pengurutan sehingga pengguna dapat melihat perubahan urutan data dengan jelas. Algoritma insertion sort digunakan karena bekerja dengan cara menyisipkan setiap data ke posisi yang tepat pada bagian data yang sudah terurut. Metode ini cocok digunakan karena sederhana dan sesuai untuk jumlah data yang tidak terlalu besar.  

# Source Code
<img width="400" height="231" alt="image" src="https://github.com/user-attachments/assets/5f223e18-d3b5-4245-bf7b-07cef019b772" />
Pada baris 1–11, baris 1 didefinisikan fungsi insertion_sort yang digunakan untuk mengurutkan data. Pada baris 2 dilakukan perulangan mulai dari indeks ke 1. Baris 3–4 menyimpan nilai sementara untuk stok (temp_stok) dan nama barang (temp_nama). Baris 5 menentukan indeks sebelumnya (j). Pada baris 6–9, dilakukan proses pergeseran data jika stok sebelumnya lebih besar dari nilai yang sedang dibandingkan. Data stok dan nama barang digeser bersamaan. Pada baris 10–11, nilai yang disimpan sebelumnya ditempatkan pada posisi yang benar.  

<img width="429" height="112" alt="image" src="https://github.com/user-attachments/assets/a3fff3d3-d082-4978-ae33-bb5f933c7e1a" />
Pada baris 13–18, baris 13 didefinisikan fungsi main() dan dilakukan validasi input jumlah barang menggunakan try dan except. Jika input tidak valid, program akan output error dan berhenti.  

<img width="203" height="42" alt="image" src="https://github.com/user-attachments/assets/4692f6af-52ab-419a-96c3-27b76799c2eb" />
Pada baris 19–20, dibuat dua list yaitu nama_barang (baris 19) dan stok_barang (baris 20) untuk menyimpan data.  

<img width="453" height="283" alt="image" src="https://github.com/user-attachments/assets/bf84a628-b2e0-4d12-af55-e2636af0a37d" />
Pada baris 21–34, dilakukan input data barang. Baris 23 meminta nama barang. Baris 24–32 digunakan untuk validasi stok menggunakan while True (baris 24) dan try except (baris 25). Jika stok negatif, program menampilkan pesan “Stok tidak boleh negatif” (baris 28). Jika pengguna memasukkan huruf, program menampilkan pesan “Input tidak valid” (baris 32). Jika valid, data disimpan ke dalam list (baris 33-34).  

<img width="439" height="76" alt="image" src="https://github.com/user-attachments/assets/4c52136f-dae4-421d-89a8-500b5a24b05c" />
Pada baris 36–38, program output stok sebelum diurutkan.  

<img width="392" height="38" alt="image" src="https://github.com/user-attachments/assets/fbb01690-c913-4cdb-8130-520d63affc04" />
Pada baris 40, fungsi insertion_sort dipanggil untuk mengurutkan data.  

<img width="441" height="78" alt="image" src="https://github.com/user-attachments/assets/294b9289-02ee-4674-872d-316ac98d3d5a" />
Pada baris 42–44, program output stok setelah diurutkan dari yang terkecil ke terbesar.  

<img width="257" height="38" alt="image" src="https://github.com/user-attachments/assets/3c3e701f-2e1d-466e-98be-095f7e7f6664" />
Pada baris 46–47, program dijalankan menggunakan if __name__ == "__main__": untuk memastikan fungsi main() yang dieksekusi.  

# Output Program
<img width="181" height="269" alt="image" src="https://github.com/user-attachments/assets/21e8b2e6-ed41-47d2-a5ee-7dc2de70c428" />
Program meminta user untuk memasukkan jumlah barang, lalu user memasukkan jumlah barang. Setelah itu, program meminta input nama barang dan jumlah stok untuk setiap barang sebanyak jumlah barang yang dimasukkan user. Pada proses ini, program juga melakukan validasi input, pada input stok jika user memasukkan data yang bukan angka misalnya huruf seperti “A”, maka program akan output pesan "Input tidak valid" dan meminta user untuk memasukkan ulang data. Jika user memasukkan nilai stok negatif misalnya -10, maka program akan output pesan "Stok tidak boleh negatif" dan meminta input ulang sampai data valid.  

<img width="266" height="159" alt="image" src="https://github.com/user-attachments/assets/437f8037-8496-439c-b0be-9c07e4048196" />
Setelah semua data dimasukkan dengan benar, program akan menampilkan stok sebelum diurutkan.  

<img width="264" height="161" alt="image" src="https://github.com/user-attachments/assets/a83595ae-790f-45cb-b960-e082bf235d0a" />
Selanjutnya, program menjalankan algoritma Insertion Sort untuk mengurutkan data berdasarkan jumlah stok, dan program akan menampilkan stok setelah diurutkan.  

# Link YouTube
https://youtu.be/5ySRO6Vtqco
