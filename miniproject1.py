MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
RESET = "\033[0m"

musik = [
    ["Tabun", "Yoasobi", "Jpop"],
    ["Luna", "Wisp", "Shoegaze"],
    ["Supernatural", "Newjeans", "Kpop"],
    ["California Love", "2Pac", "Hip Hop"],
    ["desire", "bixby", "Indie"],
    ["Helena", "My Chemical Romance", "Rock"]
]


while True:
    print(UNGU + "\nSISTEM REKOMENDASI MUSIK BERDASARKAN GENRE" + RESET)
    print("1. Lihat semua musik")
    print("2. Tambah musik")
    print("3. Ubah musik")
    print("4. Hapus musik")
    print("5. Rekomendasi berdasarkan genre")
    print("6. Keluar")

    pilihan = input("silahkan dipilih (1-6): ")

    # 1. Lihat musik
    if pilihan == "1":
        print(BIRU + "\nDAFTAR MUSIK" + RESET)

        if len(musik) == 0:
            print("Belum ada data musik.")
        else:
            for i, lagu in enumerate(musik, 1):
                print(f"{i}. {lagu[0]} - {lagu[1]} ({lagu[2]})")

    # 2. Tambah musik
    elif pilihan == "2":
        print(HIJAU + "\nTAMBAH MUSIK" + RESET)

        judul = input("Judul musik: ")
        penyanyi = input("Nama penyanyi: ")
        genre = input("Genre: ")

        musik.append([judul, penyanyi, genre])

        print("Musik berhasil ditambahkan!")

    # 3. Ubah musik
    elif pilihan == "3":
        print(KUNING + "\nUBAH MUSIK" + RESET)

        if len(musik) == 0:
            print("Belum ada data musik.")
        else:
            for i, lagu in enumerate(musik, 1):
                print(f"{i}. {lagu[0]} - {lagu[1]} ({lagu[2]})")

            while True:
                try:
                    nomor = int(input("Pilih nomor musik yang ingin diubah: "))

                    if 1 <= nomor <= len(musik):
                        break
                    else:
                        print("Nomor tidak tersedia.")

                except ValueError:
                    print("Masukkan nomor yang benar.")

            judul = input("Judul baru: ")
            penyanyi = input("Penyanyi baru: ")
            genre = input("Genre baru: ")

            musik[nomor - 1] = [judul, penyanyi, genre]

            print("Musik berhasil diubah!")

    # 4. Hapus musik
    elif pilihan == "4":
        print(MERAH + "\nHAPUS MUSIK" + RESET)

        if len(musik) == 0:
            print("Belum ada data musik.")
        else:
            for i, lagu in enumerate(musik, 1):
                print(f"{i}. {lagu[0]} - {lagu[1]} ({lagu[2]})")

            while True:
                try:
                    nomor = int(input("Pilih nomor musik yang ingin dihapus: "))

                    if 1 <= nomor <= len(musik):
                        break
                    else:
                        print("Nomor tidak tersedia.")

                except ValueError:
                    print("Masukkan nomor yang benar.")

            lagu = musik.pop(nomor - 1)

            print(f"Musik '{lagu[0]}' berhasil dihapus!")

    # 5. Rekomendasi
    elif pilihan == "5":
        print(BIRU + "\nREKOMENDASI MUSIK" + RESET)

        if len(musik) == 0:
            print("Belum ada data musik.")
        else:
        
            daftar_genre = sorted(list(set(lagu[2] for lagu in musik)))

            print("Genre yang tersedia saat ini:")
            for g in daftar_genre:
                print(f"  • {g}")

            genre = input("\nMasukkan genre yang disukai: ")

            rekomendasi = [lagu for lagu in musik if lagu[2].lower() == genre.lower()]

            if rekomendasi:
                print(f"\nRekomendasi musik genre {genre}:")
                for lagu in rekomendasi:
                    print(f"- {lagu[0]} - {lagu[1]}")
            else:
                print("\nMaaf, genre musik tidak ada.")

    # 6. Keluar
    elif pilihan == "6":
        print("\nTerima kasih, dan sampai jumpa lagi di lain waktu!")
        break

    # Menu salah
    else:
        print("Pilihan menu tidak valid. Silakan pilih 1-6.")