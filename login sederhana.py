print ("--PROGRAM LOGIN SEDERHANA--")
admin = input("Masukkan username : ")
pw = input("Masukkan password : ")

if admin == "Arik" and pw == "1234":
    print("Kamu berhasil login!") 
elif admin != "Arik" and pw == "1234":
    print ("username kamu salah")
elif admin == "Arik" and pw != "1234":
    print ("password kamu salah")
else:
    print("Login gagal")

