print("="*50)
print("       SISTEM PENGELOLAAN NILAI MAHASISWA      ")
print("="*50)


mahasiswa = []


def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 50:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa: "))
    mhs = {
        "nama": nama,
        "nilai": nilai,
        "grade": tentukan_grade(nilai)
    }
    mahasiswa.append(mhs)
    print(f"✅ Data {nama} berhasil ditambahkan!")

def tampilkan_data():
    print("\nDaftar Mahasiswa:")
    print("="*45)
    if len(mahasiswa) == 0:
        print("❌ Belum ada data.")
    else:
        for i, mhs in enumerate(mahasiswa, start=1):
            status = "Lulus" if mhs["nilai"] >= 70 else "TIDAK LULUS"
            print(f"{i}. {mhs['nama']} - Nilai: {mhs['nilai']} - Grade: {mhs['grade']} ({status})")

def hitung_rata():
    if len(mahasiswa) == 0:
        return 0
    total = sum(mhs["nilai"] for mhs in mahasiswa)
    return total / len(mahasiswa)

def cari_mahasiswa():
    if len(mahasiswa) == 0:
        print("❌ Belum ada data.")
        return
    cari = input("Masukkan nama mahasiswa yang dicari: ")
    ketemu = False
    for mhs in mahasiswa:
        if mhs["nama"].lower() == cari.lower():
            print(f"✅ {mhs['nama']} ditemukan dengan nilai {mhs['nilai']} (Grade: {mhs['grade']})")
            ketemu = True
    if not ketemu:
        print("❌ Mahasiswa tidak ditemukan.")

while True:
    print("\n" + "="*50)
    print("MENU".center(50))
    print("="*50)
    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Semua Data")
    print("3. Hitung Rata-rata Nilai")
    print("4. Cari Mahasiswa")
    print("5. Keluar")
    print("="*50)

    try:
        pilihan = int(input("Pilih menu (1-5): "))
    except ValueError:
        print("⚠️ Input harus berupa angka!")
        continue

    if pilihan == 1:
        tambah_mahasiswa()
    elif pilihan == 2:
        tampilkan_data()
    elif pilihan == 3:
        rata = hitung_rata()
        if rata > 0:
            print(f"\n📊 Rata-rata nilai kelas adalah: {rata:.2f}")
        else:
            print("❌ Belum ada data untuk dihitung.")
    elif pilihan == 4:
        cari_mahasiswa()
    elif pilihan == 5:
        print("\nTerima kasih sudah menggunakan aplikasi ini!")
        break
    else:
        print("⚠️ Pilihan tidak valid, coba lagi!")
