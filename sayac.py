import time
import sys

saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))

realsec = saniye
realmin = dakika
rearhour = saat

if saat > 0:
    dakika = dakika + saat * 60
if dakika > 0:
    saniye = saniye + dakika * 60

gecensure = 0
while True:
    time.sleep(1)
    saniye -= 1
    if saniye == 0:
        print("ALARMM ALARMMMM ",saat, " saat ", dakika, "dakika", realsec, "saniye doldu" )
        break
    else:
        print(saniye, "saniye gecti..")
        continue

