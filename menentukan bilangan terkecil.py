print ("----program cek bilangan----")
angka1 = int(input("masukkan bilangan 1 :"))
angka2 = int(input("masukkan bilangan 2 :"))
angka3 = int(input("masukkan bilangan 3 :"))

if angka1 < angka2 and angka1 < angka3:
    terkecil = angka1 
elif angka2 < angka1 and angka2 < angka3:
    terkecil = angka2
else :
    terkecil = angka3
    
print ("Bilangan terkecil adalah :", terkecil)
