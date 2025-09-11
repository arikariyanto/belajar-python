while True:
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5": 
        print("Terima kasih sudah menggunakan kalkulator!")
        break 

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        print("Hasil:", a + b)
    elif pilihan == "2":
        print("Hasil:", a - b)
    elif pilihan == "3":
        print("Hasil:", a * b)
    elif pilihan == "4":
        if b != 0:
            print("Hasil:", a / b)
        else:
            print("Error: Tidak bisa dibagi 0!")
    else:
        print("Pilihan tidak valid.")
