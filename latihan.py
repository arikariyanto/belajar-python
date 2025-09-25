print("="*50)
print("        SISTEM PEMESANAN TIKET BIOSKOP        ")
print("="*50)

film = {
    "Avengers": 50000,
    "Spiderman": 45000,
    "Batman": 40000
}

pesanan = []

def tampilkan_film():
    print("\nDaftar Film:")
    for i, (judul, harga) in enumerate(film.items(), start=1):
        print(f"{i}. {judul} - Rp{harga}")

def tambah_pesanan(nama, judul, jumlah):
    if judul in film:
        total = film[judul] * jumlah 
        pesanan.append({
            "nama": nama,
            "film": film,  
            "jumlah": jumlah,
            "total": total
        })
        print(f"✅ Pesanan tiket {judul} sebanyak {jumlah} berhasil ditambahkan.")
    else:
        print("⚠️ Film tidak tersedia.")

def tampilkan_pesanan():
    if not pesanan:
        print("⚠️ Belum ada pesanan.")
    else:
        print("\nDaftar Pesanan:")
        print("-"*40)
        for p in nama:   
            print(f"{p['nama']} - {p['film']} x{p['jumlah']} = Rp{p['total']}")

while True:
    print("\nMenu:")
    print("1. Lihat Daftar Film")
    print("2. Pesan Tiket")
    print("3. Lihat Semua Pesanan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tampilkan_film() 

    elif pilihan == "2":
        nama = input("Masukkan nama Anda: ")
        tampilkan_film()
        judul = input("Masukkan judul film: ")
        jumlah = int(input("Masukkan jumlah tiket: "))
        tambah_pesanan(nama, judul, jumlah)  

    elif pilihan == "3":
        tambah_pesanan()

    elif pilihan == "4":
        print("Terima kasih telah menggunakan sistem ini!")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
