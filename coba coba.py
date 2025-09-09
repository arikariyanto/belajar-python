
from datetime import datetime, date

def hitung_umur_detail(tanggal_lahir):
    today = date.today()

    tahun = today.year - tanggal_lahir.year
    bulan = today.month - tanggal_lahir.month
    hari = today.day - tanggal_lahir.day

  
    if hari < 0:
        bulan -= 1
       
        bulan_sebelumnya = today.month - 1 if today.month > 1 else 12
        tahun_sebelumnya = today.year if today.month > 1 else today.year - 1
        hari_dalam_bulan = (date(tahun_sebelumnya, bulan_sebelumnya % 12 + 1, 1) - date(tahun_sebelumnya, bulan_sebelumnya, 1)).days
        hari += hari_dalam_bulan

        tahun -= 1
        bulan += 12

    return tahun, bulan, hari

def main():
    print("=== Program Hitung Umur Detail ===")
    nama = input ("masukan nama Anda : ")
    tgl_input = input("Masukkan tanggal lahir (format: YYYY-MM-DD): ")

    try:
        tanggal_lahir = datetime.strptime(tgl_input, "%Y-%m-%d").date()
        tahun, bulan, hari = hitung_umur_detail(tanggal_lahir)

        # tambahan: hitung total hari hidup
        today = date.today()
        total_hari = (today - tanggal_lahir).days

        print(f"\nHalo {nama}, Umur Anda hari ini pada tanggal ({today}) Adalah {tahun} tahun, {bulan} bulan, {hari} hari.")
        print(f"Anda sudah hidup selama {total_hari} hari.\
              ")

    except ValueError:
        print("Format tanggal salah! Gunakan format YYYY-MM-DD (contoh: 2000-05-15)")

if __name__ == "__main__":
    main()
