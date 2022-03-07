# tuple

"""
değiştirilemez ve sıralı bir veri tipidir.
(1,2,3)
"""
tuple_veritipi = (1,2,3,3,4,5,6)

# ilk elemanı
print(tuple_veritipi[0])

#2. indeksten sonraki elemanı yazdır
print(tuple_veritipi[2:])

#count eleman
print(tuple_veritipi.count(3))


tuple_xyz = (1,2,3)
x,y,z = tuple_xyz
print(x,y,z)

# For Döngüsü kullanarak Tuple elemanlarına erişim sağlamak
diller = ("python", "c++", "javscript")
for eleman in diller:
    print(eleman)
    
#Belirtilen bir öğenin Tuple koleksiyonunda olup olmadığını kontrol etmek için “in” anahtar kelimesi kullanılabilir.
    
diller = ("python", "c++", "javascript")
if "c" in diller:
    print("aradığın değer tuple içinde mevcut")
    