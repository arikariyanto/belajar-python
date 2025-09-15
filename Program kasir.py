print("=== Program Kasir Sederhana ===")

daftar_barang = {
    "apel": 5000,
    "jeruk": 7000,
    "mangga": 8000,
    "pisang": 4000,
    "manggis": 6500
}

keranjang = []

def tampilkan_barang():
    print("\nDaftar Barang:")
    for barang, harga in daftar_barang.items():
        print(f"- {barang} : Rp{harga}")

def tambah_keranjang(nama, jumlah):
    if nama in daftar_barang:
        subtotal = daftar_barang[nama] * jumlah
        keranjang.append([nama, jumlah, subtotal])  
        print(f"✅ {jumlah} {nama} ditambahkan ke keranjang, subtotal Rp{subtotal}")
    else:
        print("❌ Barang tidak tersedia.")

def hitung_total():
    total = 0
    for item in keranjang:
        total += item[2]
    return total

def cetak_struk():
    print("\n" + "="*40)
    print("              STRUK BELANJA              ")
    print("="*40)
    print("Barang\tJumlah\tSubtotal")
    for item in keranjang:
        print(f"{item[0]}\t{item[1]}\tRp{item[2]}")
    total = hitung_total()
    print("="*40)
    print(f"Total belanja: Rp{total}")
    if total >= 50000:
        diskon = total * 0.1
        print(f"Diskon 10%: -Rp{int(diskon)}")
        print(f"Total bayar: Rp{int(total - diskon)}")
    else:
        print("Total bayar: Rp", total)
    print("="*40)
    print("Terima kasih sudah berbelanja!")


while True:
    tampilkan_barang()
    pilih = input("\nMasukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk keluar): ").lower()

    if pilih == "selesai":
        break

    if pilih in daftar_barang:
        try:
            jumlah = int(input("Masukkan jumlah: "))
            tambah_keranjang(pilih, jumlah)
        except ValueError:
            print("❌ Jumlah harus berupa angka!")
    else:
        print("❌ Barang tidak tersedia, coba lagi!")


if keranjang:
    cetak_struk()
else:
    print("\nKeranjang kosong, tidak ada struk untuk dicetak.")
