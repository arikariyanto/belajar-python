n = int(input("Masukkan angka batas: "))

ganjil = []
genap = []

for i in range(1, n+1):
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print(f"Bilangan ganjil: {ganjil}")
print(f"Bilangan genap: {genap}")
print(f"Jumlah bilangan ganjil: {len(ganjil)}")
print(f"Jumlah bilangan genap: {len(genap)}")
