#pandas 
"""
-veri işlemesi ve analizi
-zaman etiketli serileri ve sayısal tabloları işlemek
-hızlı güçlü ve esnek 
"""

import pandas as pd

#dictionary oluştur

dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "maas" : [100,150,240,350,110,220]}

veri = pd.DataFrame(dictionary)
print(veri)

#ilk 5 satır

print(veri.head())

#verinin sütunlarını yazdır
print(veri.columns)
 
# veri bilgisi
print(veri.info())

#istatistiksel özellikler
print(veri.describe())


#yaş sütunu
print(veri["yas"])

#sütun eklemek
veri["sehir"]  
print(veri)

#yas sütununun tüm satırları
print(veri.loc[:,"yas"])

#yas sütunu ve 3 satır
print(veri.loc[:2,"yas"])


#isim ve sehir sütunları arası  3 satır

print(veri.loc[:2,["yas","maas"]])

#satırları tersten yazdır
print(veri.loc[::-1,:])

#yas sütun with iloc
print(veri.iloc[:,1])


#ilk 3 satır yaş ve isim
print(veri.iloc[:3,[0,1]])


#filtreleme

dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "sehir": ["izmir","ankara","konya","ankara","ankara","antalya"]}


veri = pd.DataFrame(dictionary)
print(veri)

#ilk olarak yaşa göre filtre yas > 22
filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

#ortalama yas
ortalama_yas = veri.yas.mean()

veri ["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)


#birlestirme
dictionary1 = {"isim"  : ["ali","veli","kenan"],
              "yas"   : [15,16,17],
              "sehir" : ["izmir","ankara","konya"]
          }
veri1 = pd.DataFrame(dictionary1)

 #veri seti 2         
dictionary2 = {"isim"  : ["murat","ayse","hilal"],
              "yas"   : [33,45,66],
              "sehir" : ["ankara","ankara","antalya"]
          }
veri2 = pd.DataFrame(dictionary2)


#dikeyde birleştirme

veri_dikey = pd.concat([veri1, veri2], axis = 0)
          
#yatayda birleşirme

veri_yatay =pd.concat([veri1 , veri2], axis = 0)



