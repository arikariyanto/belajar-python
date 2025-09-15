def tambah(a, b):
    return a+b

def kurang(a, b):
    return a-b

def kali(a, b):
    return a*b
def bagi(a, b):
    if b != 0:
        return a/b
    else:
        return "Error: pembagian dengan nol!"

print("=== Kalkulator Sederhana ===")

while True:
    print("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Selesai")
    pilihan = int(input("Pilih menu: "))
    if pilihan == 5:
        print ("terima kasih")
        break    
    elif pilihan in [1,2,3,4]:
        x = int(input("Masukkan angka pertama: "))
        y = int(input("Masukkan angka kedua: "))    
        if pilihan == 1:
            print("Hasil:", tambah(x, y))
        elif pilihan == 2:
            print("Hasil:", kurang(x, y))
        elif pilihan == 3:
            print("Hasil:", kali(x, y))
        elif pilihan == 4:
            print("Hasil:", bagi(x, y))
    else:
        print("Pilihan tidak valid!")
