# -*- coding: utf-8 -*-

ogrenciler = ["Engin","Derin","Salih"]

print(ogrenciler[1])

ogrenciler.append("Ahmet")
ogrenciler.remove("Salih")
print(ogrenciler)

#list constructor
sehirler = list(("Kocaeli","İSTANBUL","Kocaeli"))
print(sehirler)
print("Sehirler dizisinin boyutu = " +str(len(sehirler)))

#fonksiyonlar
#print(sehirler.clear())
print("Kocaeli sayisi = "+ str(sehirler.count("Kocaeli")))
print("Kocaeli indexi = "+ str(sehirler.index("Kocaeli")))
print(sehirler.pop(1))
sehirler.insert(0,"istnbul")
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler

sehirler2[0] = "izmir"
print(sehirler)

print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print("********\n")
print(sehirler)
























