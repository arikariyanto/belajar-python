print("=== Program Manajemen Nilai Mahasiswa ===")

mahasiswa = []

while True:
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Daftar Mahasiswa")
    print("3. Hitung Rata-rata Nilai")
    print("4. Cari Mahasiswa berdasarkan Nama")
    print("5. Keluar")

    pilihan = int(input("Pilih menu (1-5): "))

    if pilihan == 5:
        print("Terima kasih! Program selesai.")
        break

    elif pilihan == 1:
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai: "))
        mahasiswa.append ((nama, nilai))   # simpan nama dan nilai ke list

    elif pilihan == 2:
        print("\nDaftar Mahasiswa:")
        for i in range(len(mahasiswa)):   # loop sesuai jumlah data
            print(f"{i+1}. Nama: {mahasiswa[i][0]}, Nilai: {mahasiswa[i][1]}")

    elif pilihan == 3:
        if len(mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            total = 0
            for mhs in mahasiswa:
                total += mhs[1]  # tambahkan nilai mahasiswa
            rata = total / len(mahasiswa)
            print(f"Rata-rata nilai: {rata}")

    elif pilihan == 4:
        cari = input("Masukkan nama mahasiswa yang dicari: ")
        ketemu = False
        for mhs in mahasiswa:
            if mhs[0] == cari:   # bandingkan dengan input cari
                print(f"Nama: {mhs[0]}, Nilai: {mhs[1]}")
                ketemu = True
        if ketemu == False:
            print("Mahasiswa tidak ditemukan.")

    else:
        print("Pilihan tidak valid, coba lagi!")
