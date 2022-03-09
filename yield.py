#Yield

""" 
-iterasyon(yineleme)
-generator
-yield



"""

liste = [1,2,3]
for i in liste:
    print(i)
    
    """
-generator yinelemeleri
generator değerleri beklekte saklamaz yeri gelince anında üretirler.


"""


generator = (x for x in range(1,4))
for i in generator:
    print(i)
    
"""
fonksiyon eğer return olarak generator döndürecekse bunu return yerine yield anahtar sözcüğü ile apar

"""

def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i

generator = createGenerator()
print(generator)

for i in generator:
    print(i)