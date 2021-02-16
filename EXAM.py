# exam modul 1 jcds 12 - rafif abdul aziz



print("####### NOMOR 1 #########")
def time_converter() :
    try : 
        time = int(input("masukkan detik: "))
        if time < 0 : 
            return "tidak menerima bilangan negatif"
        elif time >= 400000 :
            return "angka yang anda masukkan diluar jangkauan"
        else :
            hours = time // 3600
            minutes = (time // 60) % 60
            sec = time % 60
            return hours,minutes,sec
    except :
        return "masukkan angka dengan benar"

waktu = time_converter()
jam, menit, detik = waktu
print(jam, "jam", menit, "menit", detik, "detik")





