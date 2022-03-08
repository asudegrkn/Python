#koşullu ifadeler if - else

"""

"""
#büyük küçük sayıların karşılaştırılması

sayi1 = 4.0
sayi2 = 4.0

if sayi1 < sayi2:
    print("sayi 1 küçüktür sayi 2'den.")
elif sayi1> sayi2 :
    print("sayi 1 büyüktür sayi 2'den")

else:
    print("sayi 1 sayi 2 ye eşittir.")
    


liste = [1,2,3,4,5]

deger = 32

if deger in liste:
    
    print("{} değeri listenin içerisindedir".format(deger))
    
    #küme parantezinin içerisine  formatın içerisinde bulunan değer gelecek
else:
   print("{} değeri listenin içerisinde değildir.".format(deger))
 

dictionary = {"Türkiye" : "ANKARA",
              "İngiltere": "Londra",
              "İspanya": "Madrid"}    

keys = dictionary.keys()

deger = "Türkiye"

if deger in keys:
    
     print("evet")
else:
    print("hayır")
    
    
bool1 = True
bool2 = False

if bool1 or bool2: print("doğru")
else: print("yanlış")
