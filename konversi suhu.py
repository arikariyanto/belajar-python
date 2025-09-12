print("=== Program Konversi Suhu ===")

while True:
    print("Menu konversi:")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Celsius ke Reamur")
    print("4. Fahrenheit ke Celsius")
    print("5. Kelvin ke Celsius")
    print("6. Reamur ke Celsius")
    print("7. Keluar")

    pilihan = int(input("Pilih jenis konversi (1-6): "))
    if pilihan == 7:
        print("Terima kasih telah menggunakan program ini!")
    break

nilai = float(input("Masukkan nilai suhu: "))

if pilihan == 1:
    hasil = ( nilai * 9/5) + 32
    print(f"{nilai}°C = {hasil}°F")

elif pilihan == 2:
    hasil = nilai + 273.15
    print(f"{nilai}°C = {hasil}K")

elif pilihan == 3:
    hasil = nilai * 4/5
    print(f"{nilai}°C = {hasil}°Re")

elif pilihan == 4:
    hasil = (nilai - 32) * 5/9
    print(f"{nilai}°F = {hasil}°C")

elif pilihan == 5:
    hasil = nilai - 273.15
    print(f"{nilai}K = {hasil}°C")

elif pilihan == 6:
    hasil = nilai * 5/4
    print(f"{nilai}°Re = {hasil}°C")

else:
    print("Pilihan tidak valid!")
