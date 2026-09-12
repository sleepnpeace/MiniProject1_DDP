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
Kode ini berfungsi jika pengguna menginput angka 2 akan masuk ke menu ubah dan menampilkkan judul menu dengan warna kuning, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik.", tetapi jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0. 

lalu ada loop validasi (while true) berfungsi agar program meminta pengguna untuk terus menginput nomor sampai valid, terdapat penanganan error (try), input nomor dari list musik yang ingin diubah, lalu ada conditional statement lagi yaitu, jika angka list dari data musik valid loop validasi(while true) dihentikan(break), jika angka tidak valid akan muncul pesan "Nomor tidak tersedia." lalu terdapat penanganan error tipe data(except ValueError) jika data yang dimasukkan berupa simbol atau huruf dan muncul pesan "Masukkan nomor yang benar."), terdapat input judul, artis, genre untuk diubah, lalu kode yang mengganti list lama pada nomor tertentu dengan list data baru. Dikurangi 1 (nomor - 1) karena nomor di Python selalu dimulai dari angka 0, dan ada kode untuk menampilkan pesan "Musik berhasil diubah!")  

![alt text](https://github.com/sleepnpeace/MiniProject1_DDP/blob/main/Images/4.png)

![alt text](url)

![alt text](url)
