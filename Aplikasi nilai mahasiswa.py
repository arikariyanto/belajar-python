print("="*40)
print("  APLIKASI NILAI MAHASISWA SEDERHANA  ")
print("="*40)

mahasiswa = []

def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa: "))
    mahasiswa.append([nama, nilai])
    print(f"✅ Data {nama} berhasil ditambahkan!")

def hitung_rata():
    total = 0
    for mhs in mahasiswa:
        total += mhs[1]
    return total / len(mahasiswa)

while True:
    print("\n" + "="*40)
    print("MENU".center(40))
    print("="*40)
    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Semua Data")
    print("3. Hitung Rata-rata Nilai")
    print("4. Cari Mahasiswa")
    print("5. Keluar")
    print("="*40)

    pilihan = int(input("Pilih menu (1-5): "))

    if pilihan == 5:
        print("\nTerima kasih sudah menggunakan aplikasi ini!")
        break

    elif pilihan == 1:
            tambah_mahasiswa()

    elif pilihan == 2:
        print("\nDaftar Mahasiswa:")
        if len(mahasiswa) == 0:
            print("❌ Belum ada data.")
        else:
            for i in range(len(mahasiswa)):
                status = "Lulus" if mahasiswa[i][1] >= 70 else "TIDAK LULUS"
                print(f"{i+1}. {mahasiswa[i][0]} - Nilai: {mahasiswa[i][1]} ({status})")

    elif pilihan == 3:
        if len(mahasiswa) == 0:
            print("❌ Belum ada data untuk dihitung.")
        else:
            rata2= hitung_rata()
            print(f"\n📊 Rata-rata nilai: {rata2:.2f}")

    elif pilihan == 4:
        cari = input("Masukkan nama mahasiswa yang dicari: ")
        ketemu = False
        for mhs in mahasiswa:
            if mhs[0].lower() == cari.lower():
                print(f"✅ {mhs[0]} ditemukan dengan nilai {mhs[1]}")
                ketemu = True
        if not ketemu:
            print("❌ Mahasiswa tidak ditemukan.")

    else:
        print("⚠️ Pilihan tidak valid, coba lagi!")
