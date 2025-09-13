print("=== Program Kasir Sederhana ===")

daftar_barang = {
    "apel": 5000,
    "jeruk": 7000,
    "mangga": 8000,
    "pisang": 4000
}

total = 0

while True:
    print("\nDaftar Barang:")
    for barang, harga in daftar_barang.items():
        print(f"- {barang} : Rp{harga}")

    pilih = input("Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk keluar): ").lower()

    if pilih == "selesai":
        break

    if pilih in daftar_barang:
        jumlah = int(input("Masukkan jumlah: "))
        subtotal = daftar_barang[pilih] * jumlah   # isi bagian kosong
        total += subtotal
        print(f"Ditambahkan {jumlah} {pilih} ke keranjang, subtotal Rp{subtotal}")
    else:
        print("Barang tidak tersedia, coba lagi!")

print("\n=== Struk Belanja ===")
print(f"Total belanja: Rp{total}")
