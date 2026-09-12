# MiniProject1_DDP

Penjelasan Program
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/1%20warna.png)
Kode ini berfungsi untuk mendefinisikan warna yang diambil dari kode ANSI yang akan digunakan untuk setiap judul menu

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/1%20list%20musik.png)
kode ini berfungsi untuk menyimpan data musik menggunakan list dan didalam nya terdapat judul musik, artis, dan genre 

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/1%20menu%20utama.png)
Kode ini berfungsi untuk melakukan perulangan tanpa henti sampai program dihentikan, menampilkan output menu utama (list semua musik, tambah musik, ubah musik, hapus musik, rekomendasi genre, dan keluar), memberi warna untuk judul menu utama (warnanya ungu dan reset untuk batas serta mengembalikan warna ke normal), dan untuk memasukkan input angka dari 1-6

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/1.png)

Kode ini memuat conditional statement yang berfungsi jika pengguna menginput angka 1 akan masuk ke menu lihat dan menampilkkan judul menu dengan warna biru, muncul output "Belum ada data musik." jika data belum ada, dan jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/2.png)

Kode ini berfungsi jika pengguna menginput angka 2 akan masuk ke menu tambah dan menampilkkan judul menu dengan warna hijau, dan dapat menginput judul, artis, genre untuk menambahkan data ke dalam list, dan dengan append musik baru yang ditambahkan akan ditaruh di bagian terakhir dalam list utama musik, lalu kode untuk menampilkan pesan "Musik berhasil ditambahkan!)

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/3.png)
Kode ini berfungsi jika pengguna menginput angka 3 akan masuk ke menu ubah dan menampilkkan judul menu dengan warna kuning, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik.", tetapi jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0

lalu ada loop validasi (while true) berfungsi agar program meminta pengguna untuk terus menginput nomor sampai valid, terdapat penanganan error (try), input nomor dari list musik yang ingin diubah, lalu ada conditional statement lagi yaitu, jika angka list dari data musik valid loop validasi(while true) dihentikan(break), jika angka tidak valid akan muncul pesan "Nomor tidak tersedia." lalu terdapat penanganan error tipe data(except ValueError) jika data yang dimasukkan berupa simbol atau huruf muncul pesan "Masukkan nomor yang benar.")

terdapat input judul, artis, genre untuk diubah, lalu kode yang mengganti list lama pada nomor tertentu dengan list data baru. Dikurangi 1 (nomor - 1) karena nomor di Python selalu dimulai dari angka 0, dan ada kode untuk menampilkan pesan "Musik berhasil diubah!")  

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/4.png)
Kode ini berfungsi jika pengguna menginput angka 4 akan masuk ke menu hapus dan menampilkkan judul menu dengan warna merah, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik.", tetapi jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0

lalu ada loop validasi (while true) berfungsi agar program meminta pengguna untuk terus menginput nomor sampai valid, terdapat penanganan error (try), input nomor dari list musik yang ingin diubah, lalu ada conditional statement lagi yaitu, jika angka list dari data musik valid loop validasi(while true) dihentikan(break), jika angka tidak valid akan muncul pesan "Nomor tidak tersedia." lalu terdapat penanganan error tipe data(except ValueError) jika data yang dimasukkan berupa simbol atau huruf muncul pesan "Masukkan nomor yang benar.")

terdapat fungsi hapus musik berdasarkan angka yang di input dan variabel lagu untuk memanggil namanya kembali di kode untuk menampilkan pesan data musik yang sudah di hapus

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/5.png)
Kode ini berfungsi jika pengguna menginput angka 5 akan masuk ke menu rekomendasi dan menampilkkan judul menu dengan warna biru, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik. jika ada (minimal 1) akan menampilkan daftar genre yang didalamnya terdapat musik sesuai genre tersebut

lalu ada kode bertugas mengambil semua nama genre dari daftar musik, membuang genre yang ganda, lalu menyusunnya secara rapi sesuai urutan abjad (A–Z). Cara kerjanya berjalan dari dalam ke luar: program mengumpulkan seluruh genre dari tiap lagu (lagu[2] for lagu in musik), fungsi set() otomatis menghapus duplikatnya, list() mengubahnya kembali menjadi daftar biasa, dan perintah sorted() mengurutkan daftar genre tersebut dari A sampai Z sebelum disimpan ke variabel daftar_genre.

lalu ada perulangan untuk mencetak daftar genre dan menggunakan "•" sebagai bentuk pengurutannya, terdapat input genre untuk nama genre yang ingin dicari, kemudian program akan memeriksa satu per satu data musik dalam list musik, kemudian mengambil bagian lagu[2] yang merupakan genre, fungsi .lower() digunakan agar huruf besar dan kecil tidak menjadi masalah, misalnya "Rock" dan "rock" tetap dianggap sama. Musik yang genrenya cocok akan dimasukkan ke dalam list rekomendasi.

lalu ada conditional statement jika genre yang diinput ada akan menampilkan rekomendasi dengan genre yang sesuai, jika tidak muncul pesan "Maaf, genre tidak ada." dan akan kembali ke menu utama

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/6.png)
Kode ini berfungsi jika pengguna menginput angka 6 akan keluar dari program dan muncul pesan "Terima kasih, dan sampai jumpa lagi di lain waktu!"

dan kode jika kondisi menginput bukan angka 1-6 pada menu utama akan menampilkan pesan "Pilihan menu tidak valid. Silakan pilih 1-6."

-Flowchart
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/flowchart.jpg)

-Output Program
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/output%20menu%20utama.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/pilihan%20menu%20tidak%20valid.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/tampilkan%20musik.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/tambahkan%20musik.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/ubah%20musik%20berhasil.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/ubah%20musik%20tidak%20valid.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/hapus%20musik.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/hapus%20musik%20tidak%20valid.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/genre%20.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/genre%20musik%20ada.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/genre%20musik%20tidak%20ada.png)
![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/keluar.png)

