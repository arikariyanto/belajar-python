print("=== Program Kasir Sederhana ===")

daftar_barang = {
    "apel": 5000,
    "jeruk": 7000,
    "mangga": 8000,
    "pisang": 4000,
    "manggis": 6500
}

keranjang = []

while True:
    print("\nDaftar Barang:")
    for barang, harga in daftar_barang.items():
        print(f"- {barang} : Rp{harga}")

    pilih = input("Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk keluar): ").lower()

    if pilih == "selesai":
        break

    if pilih in daftar_barang:
        jumlah = int(input("Masukkan jumlah: "))
        subtotal = daftar_barang[pilih] * jumlah   
        keranjang.append((pilih,jumlah,subtotal))
        print(f"Ditambahkan {jumlah} {pilih} ke keranjang, subtotal Rp{subtotal}")
    else:
        print("Barang tidak tersedia, coba lagi!")

total = 0
for item in keranjang:
    total += item[2]

diskon = 0
if total > 50000:
    diskon = total * 0.1
    total -= diskon

print("\n=== Struk Belanja ===")
print ("barang\tJumlah\tSubtotal")
for item in keranjang:
    print(f"{item[0]}\t{item[1]}\tRp{item[2]}")

print ("------------------------")
print(f"Diskon : Rp {diskon}") 
print(f"Total belanja: Rp{total}")
