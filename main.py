import pandas as pd


class Ogrenci:

    def __init__(self, ad, soyad, ogrenci_no, ders, vize, final, ortalama, harfnotu, passexam):
        self.ad = ad
        self.soyad = soyad
        self.ogrenci_no = ogrenci_no
        self.ders = ders
        self.vize = vize
        self.final = final
        self.ortalama = ortalama
        self.harfnotu = harfnotu
        self.passexam = passexam


ogrenci_listesi = []

ad = input("Öğrenci Adı: ")
soyad = input("öğrenci Soyadı: ")
ogrenci_no = input("Öğrenci Numarası:")
ders = input("Öğrenci Dersi: ")
vize = input("Vize Puanı:")
final = input("Final Puanı:")
ortalama = int(vize)*(40/100) + int(final)*(60/100)

if ortalama >= 85:
    print("Harf Notu: AA")
    harfnotu = "AA"
elif ortalama >= 75:
    print("Harf Notu: BA")
    harfnotu = "BA"
elif ortalama >= 70:
    print("Harf Notu: BB")
    harfnotu = "BB"
elif ortalama >= 65:
    print("Harf Notu: CB")
    harfnotu = "CB"
elif ortalama >= 60:
    print("Harf Notu: CC")
    harfnotu = "CC"
elif ortalama >= 55:
    print("Harf Notu: DC")
    harfnotu = "DC"
elif ortalama >= 50:
    print("Harf Notu: DD")
    harfnotu = "DD"
elif ortalama <= 50:
    print("Harf Notu: FF")
    harfnotu = "FF"


if ortalama < 50:
    print("Sonuç :{0} ".format(ortalama), ad+" "+soyad+" "+harfnotu, "harf notu ile KALDINIZ!")
    passexam = "Kaldınız"
else:
    print("Sonuç :{0} ".format(ortalama), "Tebrikler", "", ad+" "+soyad+" "+harfnotu, "harf notu ile GEÇTİNİZ!")
    passexam = "Geçtiniz"

ogrenci_listesi.append(Ogrenci(ad, soyad, ogrenci_no, ders, vize, final, ortalama, harfnotu, passexam))

print(ogrenci_listesi)

df = pd.DataFrame([t.__dict__ for t in ogrenci_listesi])
print(df)


df.to_excel("ogrenci_listesi1.xlsx")
df.to_excel('pandas_to_excel.xlsx', sheet_name='ogrenci_listesi')
