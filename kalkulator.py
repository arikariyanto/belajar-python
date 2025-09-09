# kalkulator_terminal.py
import os

# Tambahan warna agar lebih menarik
class Warna:
    HEADER = "\033[95m"
    BIRU = "\033[94m"
    HIJAU = "\033[92m"
    KUNING = "\033[93m"
    MERAH = "\033[91m"
    RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def kalkulator():
    while True:
        clear()
        print(Warna.HEADER + "="*35)
        print("     KALKULATOR TERMINAL SEDERHANA")
        print("="*35 + Warna.RESET)
        print(Warna.BIRU + "Operator yang tersedia: +, -, *, /" + Warna.RESET)

        try:
            angka1 = float(input(Warna.KUNING + "Masukkan angka pertama: " + Warna.RESET))
            operator = input(Warna.KUNING + "Masukkan operator (+, -, *, /): " + Warna.RESET)
            angka2 = float(input(Warna.KUNING + "Masukkan angka kedua: " + Warna.RESET))

            if operator == '+':
                hasil = angka1 + angka2
            elif operator == '-':
                hasil = angka1 - angka2
            elif operator == '*':
                hasil = angka1 * angka2
            elif operator == '/':
                if angka2 != 0:
                    hasil = angka1 / angka2
                else:
                    print(Warna.MERAH + "Error: Pembagian dengan nol tidak diperbolehkan!" + Warna.RESET)
                    input("\nTekan Enter untuk melanjutkan...")
                    continue
            else:
                print(Warna.MERAH + "Operator tidak valid!" + Warna.RESET)
                input("\nTekan Enter untuk melanjutkan...")
                continue

            print(Warna.HIJAU + f"\nHasil: {angka1} {operator} {angka2} = {hasil}" + Warna.RESET)

        except ValueError:
            print(Warna.MERAH + "Input harus berupa angka!" + Warna.RESET)

        # Pilihan melanjutkan
        lanjut = input(Warna.BIRU + "\nHitung lagi? (y/n): " + Warna.RESET).lower()
        if lanjut != 'y':
            print(Warna.HIJAU + "\nTerima kasih sudah menggunakan kalkulator! 👋" + Warna.RESET)
            break

if __name__ == "__main__":
    kalkulator()