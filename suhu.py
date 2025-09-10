print("PROGRAM MENGHITUNG SUHU")

celcius = float(input("masukkan suhu dalam celcius :"))

if celcius < 0:
    print ("suhu sekarang adalah beku")
elif celcius <30:
    print ("suhu sekarang adalah normal")
else :
    print ("suhu sekarang adalah panas")

fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
reamur = celcius * 4/5

print ("suhu dalam Fahrenheit:", fahrenheit, "°F")
print ("suhu dalam Kelvin:", kelvin, "°k")
print ("suhu dalam Reamur:", reamur, "°Re")
    
