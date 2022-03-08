#Döngüler 
"""
bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.
diziler: liste, tuple, string, dictionary, numpy pandas veri tipleri

"""

#FOR

for i in range(1,11):
    print(i)

liste  = [1,4,5,6,8,3,3,4,67]
print(sum(liste))


toplam = 0
for c in liste:
  toplam = toplam + c
  
print(toplam)

"""
0=0+1
1=1+4
5= 5+6
11= 11+8
19 = 19+....
"""

tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)
    
#™while
i=0
while i < 4:
    print(i)
    i=i+1

liste = [1,4,5,6,8,3,3,4,67]
sinir = len(liste)


her  = 0
hesapla = 0
while her < sinir:
    hesapla = hesapla + liste[her]
    her = her + 1
    print(hesapla)
    
