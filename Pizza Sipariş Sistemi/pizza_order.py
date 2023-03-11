# Saygin Aytemiz
# saygin.aytemiz@gmail.com
# Global AI Hub Akbank-Python-Bootcamp 
# Pizza Siparis Sistemi Projesi
# Mart 2023

"""
Proje hakkinda : 
    
* Oncelikle kullanici menuden pizza tabani ve sos secmektedir. Ardindan 
yaptigi secimlerin aciklamasi ve toplam tutari kullaniciya gosterilir. 
* Devaminda kullanicidan bazi bilgilerinin girilmesi istenmektedir. Odeme 
alindiktan sonra kullaniciya ait bu bilgiler veri tabanina eklenmektedir. 
* Sistem, kullanicilarin menudeki pizzayi ve istedikleri sosu secmesiyle baslar.
* Kullanicilar odemelerini kredi karti ile yapmaktadir.
* Her pizzanin ve sosun kendine ait bir aciklamasi ve fiyati vardir. 
* Islemlere devam edilebilmesi icin bilgilerin dogru bir sekilde girilmesi 
gerekmektedir. Aksi takdirde bilginin tekrar girilmesi istenir.
* Islemler tamamlandiktan sonra siparisin basariyla olusturuldugunu belirten
mesaj kullaniciya gosterilir.


"""

# Gerekli kitapliklarin ice aktarilmasi
import csv
from datetime import datetime


#  Madde 3 - Menu.txt adli bir dosya olusturma ve icine metni yazdirma
menu = open("menu.txt", "w")
menu.write("""

*******  Kopernik Pizza'ya Hosgeldiniz!  *******

  * Lutfen Bir Pizza Tabani Seciniz:

    1: Klasik
    2: Margarita
    3: Turk Pizza
    4: Sade Pizza

  * ve sececeginiz sos:

    11: Zeytin
    12: Mantar
    13: Keci Peyniri
    14: Et
    15: Sogan
    16: Misir

   * Tesekkur ederiz!
""")
menu.close()


# Madde 4 - "Pizza" ust sinifi olusturma ve encapsulation
class Pizza:
    def __init__(self, aciklama, ucret):
        self.__aciklama = aciklama
        self.__ucret = ucret

    def get_aciklama(self):
        return self.__aciklama

    def get_ucret(self):
        return self.__ucret
    
# Madde 5 - Pizza turleri icin alt sinif olusturma
class klasik_pizza(Pizza):
    def __init__(self):
        aciklama = "Klasik Pizza"
        ucret = 89.99
        super().__init__(aciklama, ucret)

class margarita_pizza(Pizza):
    def __init__(self):
        aciklama = "Margarita Pizza"
        ucret = 109.99
        super().__init__(aciklama, ucret)

class turk_pizza(Pizza):
    def __init__(self):
        aciklama = "Turk Pizza"
        ucret = 99.99
        super().__init__(aciklama, ucret)

class sade_pizza(Pizza):
    def __init__(self):
        aciklama = "Sade Pizza"
        ucret = 79.99
        super().__init__(aciklama, ucret)
        
        
# Madde 6 - Tum sos siniflarinin super sinifi "Decorator"
class Decorator(Pizza):
    def get_aciklama(self):
        return self.pizza.get_aciklama() +  " ve " + self.aciklama
    
    def get_ucret(self):
        return self.ucret + self.pizza.get_ucret()   
    
# Sos siniflarinin olusturulmasi
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Zeytin"
        self.ucret =  9.99
    
      
class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Mantar"
        self.ucret =  19.99
    

class Keci_peyniri(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Keci Peyniri"
        self.ucret = 29.99
    

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Et"
        self.ucret = 49.99
    
    
class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Sogan"
        self.ucret = 9.99
    

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__
        self.pizza = pizza
        self.aciklama = "Misir"
        self.ucret = 9.99



# main fonksiyonu
def main():
    # Menunun ekrana yazdirilmasi
    menu = open("menu.txt", "r")
    print(menu.read())

    # Pizza secimi
    while True:
        pizza_secimi = input("\nPizza seciminizi girin: ")
        if pizza_secimi == "1":
            pizza = klasik_pizza()
            break
        elif pizza_secimi == "2":
            pizza = margarita_pizza()
            break 
        elif pizza_secimi == "3":
            pizza = turk_pizza()
            break
        elif pizza_secimi == "4":
            pizza = sade_pizza()      
            break
        else:    
            print("\n****Secilen pizza mevcut degil. Tekrar secim yapiniz.****")
            
    # Sos ekleme
    while True: 
        sos_secimi = input("\nSos seciminizi girin: ")
        if sos_secimi == "11":
            pizza = Zeytin(pizza)
            break
        elif sos_secimi == "12":
            pizza = Mantar(pizza)
            break
        elif sos_secimi == "13":
            pizza = Keci_peyniri(pizza)
            break
        elif sos_secimi == "14":
            pizza = Et(pizza)
            break
        elif sos_secimi == "15":
            pizza = Sogan(pizza)
            break
        elif sos_secimi == "16":
            pizza = Misir(pizza)
            break
        else:
            print("\n**** Secilen sos mevcut degil, tekrar secim yapiniz..****")
            
    # Toplam fiyat hesabı
    total_ucret = round(pizza.get_ucret(),2)
    print(f"\n **** {pizza.get_aciklama()} sectiniz. ****")
    print(f"\n **** Toplam tutar: {total_ucret} TL ****")

    # Kullanici bilgilerini alma kismi
    while True:
        ad = input("\nIsminizi giriniz: ")
        if ad.strip().isdigit():
            print("\n**** Adinizda rakam bulunmamalidir. Tekrar deneyin.****")
        else:
            break

    while True:
        tc_numara = input("\nTC kimlik numaranizi giriniz: ")
        if tc_numara.strip().isdigit():
            break
        else:
            print("\n**** TC kimlik numaraniz yalnizca rakamlardan olusmalidir. Tekrar deneyin.****")
            
    while True:
        kredi_kartNo = input("\nKredi karti numaranizi giriniz: ")
        if kredi_kartNo.strip().isdigit():
            break
        else:
            print("\n**** Kredi karti numaraniz yalnizca rakamlardan olusmalidir. Tekrar deneyin.****")
            
    while True:
        kredi_kartSifre = input("\nKredi karti sifrenizi giriniz: ")
        if kredi_kartSifre.strip().isdigit():
            break
        else:
            print("\n**** Kart sifreniz yalnizca rakamlardan olusmalidir. Tekrar deneyin.****")
            
    # Veritabani
    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ad, tc_numara, kredi_kartNo, pizza_secimi + " numarali pizza" ,  sos_secimi + " numarali sos", order_time, kredi_kartSifre])
    print("\n **** Siparisiniz basariyla kaydedildi. ****")
    print(" **** Tekrar bekleriz. ****")

if __name__ == "__main__":
    main()

