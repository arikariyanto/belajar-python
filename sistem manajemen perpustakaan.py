print("="*40)
print("==== Sistem Manajemen Perpustakaan ====")
print("="*40)


buku = []

while True:
    print("\n" + "="*40)
    print("\nMenu:")
    print("="*40)
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Cari Buku")
    print("6. Keluar")
    print("="*40)

    pilihan = int(input("Pilih menu (1-6): "))

    if pilihan == 6:
        print("\n" + "="*40)
        print("Terima kasih sudah menggunakan sistem perpustakaan!".center(40))
        print("="*40)
        break

    elif pilihan == 1:
        print("\n" + "="*40)
        judul = input("Masukkan judul buku: ")
        stok = int(input("Masukkan jumlah stok: "))
        buku.append([judul, stok]) 
        print(f"\n✅ Buku '{judul}' berhasil ditambahkan dengan stok {stok}.")

    elif pilihan == 2:
        print("\n" + "="*40)
        print("\nDaftar Buku:")
        if len(buku) == 0:
            print("❌ Belum ada buku di perpustakaan.")
        else:
            for i in range(len(buku)):
                print(f"{i+1}. {buku[i][0]} - Stok: {buku[i][1]}")

    elif pilihan == 3:
        print("\n" + "="*40)
        pinjam = input("Masukkan judul buku yang ingin dipinjam: ")
        ketemu = False
        for item in buku:
            if item[0] == pinjam and item[1] > 0:  
                item[1] -= 1
                print(f"\n📚 Anda berhasil meminjam buku {pinjam}")
                ketemu = True
        if not ketemu:
            print("\n❌ Buku tidak tersedia atau stok habis.")

    elif pilihan == 4:
        print("\n" + "="*40)
        kembali = input("Masukkan judul buku yang ingin dikembalikan: ")
        ketemu = False
        for item in buku:
            if item[0] == kembali : 
                item[1] += 1
                print(f"\n📚 Berhasil mengembalikan buku {kembali}")
                ketemu = True
        if not ketemu:
            print("❌ Buku tidak ditemukan di daftar.")

    elif pilihan == 5:
        print("\n" + "="*40)
        cari = input("Masukkan judul buku yang dicari: ")
        ketemu = False
        for item in buku:
            if item[0] == cari:   
                print(f"\n✅ Buku ditemukan: {item[0]} - Stok: {item[1]}")
                ketemu = True
        if not ketemu:
            print("❌ Buku tidak ditemukan.")

    else:
        print("\n⚠️Pilihan tidak valid, coba lagi!")

