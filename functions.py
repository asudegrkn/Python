#Fonksiyonlar
"""
-Karmaşık işlemleri toplar ve tek adımda yapmamızı sağlar
-şablon
+düzenleme

"""


def daireAlan(r):
    """

    Parameters
    ----------
    r : int - daire yarıçapı.
        

    Returns
    -------
    daire_alani : float - daire alanı.

    """
    pi = 3.14
    daire_alani = pi*(r**2)
    
    return daire_alani

daireAlaniDegiskeni = daireAlan(3)

print(daireAlaniDegiskeni)

"""
classların içerisinde kullanılıyorsa method
classların dışarısında kullanılıyorsa fonksiyon deniliyor 
fakat yapısal olarak aynılar.

"""



def daireCevre(r, pi = 3.14):
     """

    Parameters
    ----------
    r : int - daire yarıçapı.
    pi: float - pi sayısı   

    Returns
    -------
    daire_cevre : float - daire çevresi.

    """
    
    daire_cevre = 2*pi*r
    
    return daire_cevre

daireCevre = daireCevre(3)
print(daireCevre)
    
    
katsayi = 5


def katsayiCarpimi():
    
    
    global katsayi                      
    print (katsayi*kaysayi)

katsayiCarpimi()
print(katsayi)
    


#boş fonksiyonlar

def bos():
    pass
    
    
#built in fonk.
    
liste = [1,2,3,4]

print(len(liste))
print(str(liste))
liste2 = liste.copy()
print(liste2)
print(max(liste2))

print(min(liste2))

#lambd fonk.
"""
- ileri seviyeli
-küçük ve anonim işlemdir 
"""
def carpma(x,y,z):
    return x*y*z

sonuc = carpma(2,3,4)  
print(sonuc)   


#aynı işlem with lambda
fonksiyon_lambda = lambda x,y,z : x*y*z
sonuc2 = fonksiyon_lambda(2,3,4)
print(sonuc2)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    