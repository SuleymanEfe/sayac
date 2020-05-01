import time
import sys

while True:
    saat = int(input("Saat: "))
    if saat < 0:
        print("Saat en az 0 olabilir. Lutfen tekrar girin.")
        continue
    elif saat > 24:
        print("Saat en fazla 24 olabilir. Lutfen tekrar girin.")
        continue
    else:
        break

while True:
    dakika = int(input("Dakika: "))
    if dakika < 0:
        print("Dakika en az 0 olabilir. Lutfen tekrar girin.")
        continue
    elif dakika > 60:
        print("Dakika en fazla 60 olabilir. Lutfen tekrar girin. ")
        continue
    else:
        break

while True:
    saniye = int(input("Saniye: "))
    if saniye < 0:
        print("Saniye en az 0 olabilir. Lutfen tekrar girin.")
        continue
    elif saniye > 60:
        print("Saniye en fazla 60 olabilir. Lutfen tekrar girin.")
        continue
    else:
        break


saatkayit = saat
dakikakayit = dakika
saniyekayit = saniye


kontrol = 0

while True:
    time.sleep(1)
    saniye -= 1
    if saniye == 0:
        if dakika != 0:
            dakika -= 1
            saniye = 59
        elif saat != 0:
            saat -= 1
            dakika = 59
            saniye = 59
        else:
            kontrol = 1

    if kontrol == 1:
        print("Sayac bitti... ", saatkayit, " saat ", dakikakayit, "dakika", saatkayit, "saniye doldu" )
        break
    else:
        if saat != 0:
            print(saat, "saat ", dakika, "dakika", saniye, "saniye kaldi..")
        elif dakika != 0:
            print(dakika, "dakika", saniye, "saniye kaldi..")
        else:
            print(saniye, "saniye kaldi..")
        continue

