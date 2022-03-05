# Listeler

"""
composite data type ve çok yönlüdür.
farklı data typeları içerisinde barındırabilir.

"""

liste = [1,2,3,4,5,6]
print(type(liste))

hafta = ["pazartesi","salı","çarşamba","perşembe","cuma","cumartrsi","pazar"]
#ilk eleman
print(hafta[0])

#son eleman 

print(hafta[6])
print(len(hafta))  #eleman sayısı
print(hafta[len(hafta)-1])
print(hafta[-1])

#liste 2-34 ; 1,2,3 indeks
print(hafta[1:4]) #1den 4 e kadar 1 dahil 4 değil

#sayı listesi
sayi_listesi = [1,2,3,4,5,6]
sayi_listesi.append(7)  #eleman ekleme

print(sayi_listesi)

#eleman çıkartma
sayi_listesi.remove(4)
print(sayi_listesi)

#listeyi ters çevir
sayi_listesi.reverse()
print(sayi_listesi)

#listeyi sırala
sayi_listesi = [11,1,2,3,4,60,7,0]
sayi_listesi.sort()
print(sayi_listesi)
