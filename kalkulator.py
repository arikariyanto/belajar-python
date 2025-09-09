# kalkulator_sederhana.py

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Operator yang tersedia: +, -, *, /")
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))

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
                print("Error: Pembagian dengan nol tidak diperbolehkan!")
                return
        else:
            print("Operator tidak valid!")
            return

        print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")

    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    kalkulator()
