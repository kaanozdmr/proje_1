from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import os


def k_kucuk():
    def k_kucuk_func(k, liste):
        sirali_liste = sorted(liste)
        if k <= len(sirali_liste):
            return sirali_liste[k - 1]
        else:
            return 0

    print("k’nıncı En Küçük Elemanı Bulma")
    k = int(input("k değerini girin: "))
    liste = input("Listeyi virgülle ayırarak girin: (Örneğin, \"1,2,3\") ").split(',')
    liste = [int(x.strip()) for x in liste]
    sonuc = k_kucuk_func(k, liste)
    if sonuc != 0:
        print(k,". en küçük eleman: ",sonuc)
    else:
        print("Geçersiz k değeri.")
    input("Devam etmek için ENTER tuşuna basın...")  

def en_yakin_cift():
    def en_yakin_cift_fonk(hedef, liste):
        liste.sort()
        en_yakin = float('inf')
        en_yakin_cift = None

        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                toplam = liste[i] + liste[j]
                fark = abs(hedef - toplam)

                if fark < en_yakin:
                    en_yakin = fark
                    en_yakin_cift = (liste[i], liste[j])

        return en_yakin_cift
    print("En Yakın Çifti Bulma")
    hedef = int(input("Liste içindeki herhangi iki sayının toplamı: "))
    liste = input("Listeyi virgülle ayırarak girin:(Örneğin, \"1,2,3\") ").split(',')
    liste = [int(x.strip()) for x in liste]

    sonuc = en_yakin_cift_fonk(hedef, liste)

    if sonuc != 0:
        print("En yakın çift: ",sonuc[0] ,"ve" ,sonuc[1])
    else:
        print("Liste boş veya geçersiz hedef değeri.")
    input("Devam etmek için ENTER tuşuna basın...")
def tekrar_eden_elemanlar():
    def tekrar_eden_elemanlar_fonk(liste):
        tekrar_edenler = [x for x in liste if liste.count(x) > 1]
        sonuc = sorted(list(set(tekrar_edenler)))
        return sonuc
    print("Bir Listenin Tekrar Eden Elemanlarını Bulma")
    liste = input("Listeyi virgülle ayırarak girin:(Örneğin, \"1,2,3\") ").split(',')
    liste = [int(x) for x in liste]
    sonuc = tekrar_eden_elemanlar_fonk(liste)
    print("Tekrar eden elemanlar:", sonuc)
    input("Devam etmek için ENTER tuşuna basın...")

def matris_carpimi():
    def matris_carpimi_fonk(A, B):
        sonuc = [[sum(a * b for a, b in zip(satir, sutun)) for sutun in zip(*B)] for satir in A]
        return sonuc
    print("Matris Çarpımı")
    A = []
    B = []
    as1 = int(input("A matrisinin satır sayısını girin: "))
    as2 = int(input("A matrisinin sütun sayısını girin: "))
    print("A matrisinin elemanlarını girin:")
    for i in range(as1):
        satir = input(f"{i + 1}. satırı girin (örn. \"1,2,3\"): ").split(",")
        A.append([int(x) for x in satir])

    bs1 = int(input("B matrisinin satır sayısını girin: "))
    bs2 = int(input("B matrisinin sütun sayısını girin: "))
    print("B matrisinin elemanlarını girin:")
    for i in range(bs1):
        satir = input(f"{i + 1}. satırı girin (örn. \"1,2,3\"): ").split(",")
        B.append([int(x) for x in satir])
    if as2 != bs1 or as1 != bs2:
        print("A matrisinin sütun sayısı ile B matrisinin satır sayısı uyuşmuyor. Matris çarpımı yapılamaz.")
    else:
        sonuc = matris_carpimi_fonk(A, B)
        for satir in sonuc:
            print(satir)
    input("Devam etmek için ENTER tuşuna basın...")

def en_kucuk_deger():
    def en_kucuk_deger_fonk(liste):
        if len(liste) == 1:
            return liste[0]
        else:
            min_deger = en_kucuk_deger_fonk(liste[1:])
            if liste[0] < min_deger:
                return liste[0]
            else:
                return min_deger
    print("Liste İçinde En Küçük Değeri Bulma")
    liste = input("Listeyi virgülle ayırarak girin:(Örneğin, \"1,2,3\") ").split(',')
    liste = [int(x) for x in liste]
    sonuc = en_kucuk_deger_fonk(liste)
    print("en küçük değer:", sonuc)
    input("Devam etmek için ENTER tuşuna basın...")

def karekok():
    def karekok_fonk(N, x0, tol=10**-10, maxiter=10, iterasyon=0):
        hata = abs(x0 ** 2 - N)
        
        if hata <= tol or iterasyon >= maxiter:
            if iterasyon >= maxiter:
                print(maxiter ," iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin.")
            return x0
        
        x0 = 0.5 * (x0 + N / x0)
        return karekok_fonk(N, x0, tol, maxiter, iterasyon + 1)
    print("Karekök Fonksiyonu")
    N = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
    x0 = float(input("x0 girin: "))
    tol = float(input("Tolerans `tol`. Varsayılan değer 10^(-10).:(atlamak için ENTER tuşuna basın.) ") or 10 ** (-10))
    maxiter = int(input("Azami iterasyon sayısını girin (varsayılan değer 10):(Atlmaak için ENTER tuşuna basın.) ") or 10)
    sonuc = karekok_fonk(N, x0, tol, maxiter)
    print(N,"sayısının karekökü için en iyi tahmin: ",sonuc)
    input("Devam etmek için ENTER tuşuna basın...")

def eb_ortak_bolen():
    def eb_ortak_bolen_fonk(a, b):
        if b == 0:
            return a
        else:
            return eb_ortak_bolen_fonk(b, a % b)
    print("En Büyük Ortak Bölen")
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = eb_ortak_bolen_fonk(sayi1, sayi2)
    print("En büyük ortak bölen:" ,sonuc)
    input("Devam etmek için ENTER tuşuna basın...")

def asal_veya_degil():
    def asal_veya_degil_fonk(sayi, b=2):
        if sayi <= 1:
            return False
        if sayi == 2:
            return True
        if sayi % b == 0:
            return False
        if b * b > sayi:
            return True
        return asal_veya_degil_fonk(sayi, b + 1)
    sayi = int(input("Lütfen bir sayı girin: "))
    if asal_veya_degil_fonk(sayi):
        print(sayi ,"asaldır.")
    else:
        print(sayi ,"asal değildir.")
    input("Devam etmek için ENTER tuşuna basın...")


def frekans_bul():                                           
    def kelime_sayisi_hesapla(dosya_adı):
        kelime_sayac = {}
        with open(dosya_adı, 'r') as dosya:
            metin = dosya.read()
            kelimeler = metin.split()
            for kelime in kelimeler:
                kelime = kelime.strip('.,!?";()[]{}:')
                kelime = kelime.lower()
                if kelime in kelime_sayac:
                    kelime_sayac[kelime] += 1
                else:
                    kelime_sayac[kelime] = 1
        return kelime_sayac

    print("Dosya Adı Girin ve Kelime Sayısını Hesaplayın")
    dosya_adı = input("Metin dosyasının adını girin: ")
    if os.path.isfile(dosya_adı):
        kelime_sayac = kelime_sayisi_hesapla(dosya_adı)
        for kelime, sayi in kelime_sayac.items():
            print(kelime,":" , sayi ,"kez")
    else:
        print(dosya_adı ," adında bir dosya bulunamadı.")
    input("Devam etmek için ENTER tuşuna basın...")

def fibonacci():
    def hizlandirici(n, k=0, fibk=0, fibk1=1):
        if n == k:
            return fibk
        else:
            return hizlandirici(n, k+1, fibk1, fibk+fibk1)
    try:
        n = int(input("n (kaçıncı Fibonacci sayısı hesaplanacak olan): "))
        k = int(input("k : "))
        fib_k = int(input("fib_k: "))
        fib_k1 = int(input("fib_k1: "))
        sonuc = hizlandirici(n, k, fib_k, fib_k1)
        print("Fibonacci sayısı: ",sonuc)
    except ValueError:
        print("Geçersiz giriş. Bir pozitif tamsayı girin.")
    input("Devam etmek için ENTER tuşuna basın...")    


def main():
    menu = ConsoleMenu("Ana Menü")

    function_item1 = FunctionItem("k’nıncı En Küçük Elemanı Bulma", k_kucuk)
    function_item2 = FunctionItem("En Yakın Çifti Bulma:", en_yakin_cift)
    function_item3 = FunctionItem("Bir Listenin Tekrar Eden Elemanlarını Bulma:",tekrar_eden_elemanlar)
    function_item4 = FunctionItem("Matris Çarpımı:",matris_carpimi)
    function_item5 = FunctionItem("Dosya Adı Girin ve Kelime Sayısını Hesaplayın", frekans_bul)           
    function_item6 = FunctionItem("Liste İçinde En Küçük Değeri Bulma:",en_kucuk_deger)
    function_item7 = FunctionItem("Karekök Fonksiyonu:",karekok)
    function_item8 = FunctionItem("En Büyük Ortak Bölen:",eb_ortak_bolen)
    function_item9 = FunctionItem("Asallık Testi:",asal_veya_degil)
    function_item10 = FunctionItem("Fibonacci Hesapla", fibonacci)

    menu.append_item(function_item1)
    menu.append_item(function_item2)
    menu.append_item(function_item3)
    menu.append_item(function_item4)
    menu.append_item(function_item5)                                                                      
    menu.append_item(function_item6)
    menu.append_item(function_item7)
    menu.append_item(function_item8)
    menu.append_item(function_item9)
    menu.append_item(function_item10)

    menu.show()

    print("Programdan çıkılıyor...")  

if __name__ == "__main__":
    main()