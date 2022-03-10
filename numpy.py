# Numpy Kütüphanesi

"""
-marisler için hesaplama kolaylığı sağlar.
"""

import numpy as np


#1*15 boyutunda bir array-dizi

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) #array'in boyutu

dizi2 = dizi.reshape(3, 5)


print("şekil:" , dizi2.shape)
print("boyut:",dizi2.ndim)
print("veri tipi:" , dizi2.dtype.name)
print("boy:",dizi2.size)

#array type
print("type:", type(dizi2)) 

#2 boyutlu bir arrayin oluşturulması

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(dizi2D)

#sıfırlardan oluşan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

#birlerden oluşan bir array
bir_dizi = np.ones((3,4))
print(bir_dizi)

#boş array
#sıfıra ne kadar yakınsa o kadar boş
bos_dizi = np.empty((3,4))
print(bos_dizi)

#arange (x,y,basamak) 
dizi_aralik = np.arange(10,50,5) #10 dan 50 ye kadar 5 er 5 er say
print(dizi_aralik)


#linspace(x,y basamk)
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)



#float array

float_array = np.float32([[1,2],[3,4]])
print(float_array)


#matematikel işlemler

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a*b)
print(a-b)

#dizi elemanı toplama
print(np.sum(a))

#dizi içerisindeki max ı bulma
print(np.max(a))


#dizi içerisindeki min ı bulma
print(np.min(a))

#ortalama

print(np.mean(a))

#medyan"ortadaki sayı"

#dizi içerisindeki max ı bulma
print(np.median(a))

#rastgele sayı üretme [0,1] arasında sürekli uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

#index 
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk dört elemanı
print(dizi[0:4])

#dizinin tersi
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1. satır ve 1. sütununda bulunan elemanı 
print(dizi2D[1,1])

#dizinin 1. sütun ve tüm satırlar
print(dizi2D[:,1])

#1.satır , 1.2.3. sütun
print(dizi2[1,1:4])

#dizinin son satırının tüm sütunları
print(dizi2D[-1,:])


##
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)


#diziyi vektör haline getirme

vektor = dizi2D.ravel()
print(vektor)

#maksimum sayınnın indeksini bulma

maksimum_sayinin_indeksi = vektor.argmax()
print(maksimum_sayinin_indeksi)












