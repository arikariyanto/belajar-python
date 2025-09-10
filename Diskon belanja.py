print ("^^^diskon belanjaan^^^")

a = int (input ("masukkan total belanjaan anda : "))

if a >= 100000:
    diskon = 0.10
elif a >= 50000:
    diskon = 0.5
else :
    diskon = 0.0

potongan = a * diskon
total = a - potongan

print ("selamat anda mendapatkan diskon : Rp.", (potongan))
print ("total belanjaan yang perlu anda bayarkan menjadi : Rp.", (total))