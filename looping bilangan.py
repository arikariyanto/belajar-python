n = int (input("masukkan angka :"))

count = 0
print ("\nbilangan kelipatan 3 dari 1 sampai" ,n)

for i in (range (1, n)):
    if i % 3 == 0:
     print (i)
     count += 1

print (f"\nJumlah bilangan kelipatan 3 sampai {n} adalah {count}")
