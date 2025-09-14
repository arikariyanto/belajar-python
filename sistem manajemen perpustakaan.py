print("=== Sistem Manajemen Perpustakaan Sederhana ===")

buku = []

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Cari Buku")
    print("6. Keluar")

    pilihan = int(input("Pilih menu (1-6): "))

    if pilihan == 6:
        print("Terima kasih sudah menggunakan sistem perpustakaan!")
        break

    elif pilihan == 1:
        judul = input("Masukkan judul buku: ")
        stok = int(input("Masukkan jumlah stok: "))
        buku.append([judul, stok]) 

    elif pilihan == 2:
        print("\nDaftar Buku:")
        if len(buku) == 0:
            print("Belum ada buku di perpustakaan.")
        else:
            for i in range(len(buku)):
                print(f"{i+1}. {buku[i][0]} - Stok: {buku[i][1]}")

    elif pilihan == 3:
        pinjam = input("Masukkan judul buku yang ingin dipinjam: ")
        ketemu = False
        for item in buku:
            if item[0] == pinjam and item[1] > 0:  
                item[1] -= 1
                print(f"Berhasil meminjam {pinjam}")
                ketemu = True
        if not ketemu:
            print("Buku tidak tersedia atau stok habis.")

    elif pilihan == 4:
        kembali = input("Masukkan judul buku yang ingin dikembalikan: ")
        ketemu = False
        for item in buku:
            if item[0] == kembali : 
                item[1] += 1
                print(f"Berhasil mengembalikan {kembali}")
                ketemu = True
        if not ketemu:
            print("Buku tidak ditemukan di daftar.")

    elif pilihan == 5:
        cari = input("Masukkan judul buku yang dicari: ")
        ketemu = False
        for item in buku:
            if item[0] == cari:   
                print(f"Buku ditemukan: {item[0]} - Stok: {item[1]}")
                ketemu = True
        if not ketemu:
            print("Buku tidak ditemukan.")

    else:
        print("Pilihan tidak valid, coba lagi!")
