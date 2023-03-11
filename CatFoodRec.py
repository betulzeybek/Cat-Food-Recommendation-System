YAVRU_MAMA = 50
YETISKIN_MAMA = 55
KISIR_MAMA = 60
KG_YUZDE_0_3 = 3.5 / 100
KG_YUZDE_4_6 = 3 / 100
KG_YUZDE_7_12 = 2.5 / 100
KG_YUZDE_13 = 1.5 / 100

kedi_ay = int(input("Kedinizin kaç aylık olduğunu giriniz:"))
kedi_agirlik = float(input("Kedinizin ağırlığını kg cinsinden giriniz:"))
kedi_agirlik = kedi_agirlik * 1000 # İşlem kolaylığı açısından kilogramı grama çevirme işlemi yapıldı.

if kedi_ay <= 12:
    mama_fiyat = YAVRU_MAMA
    mama_turu = "Yavru Maması"
else:
    kisir = input("Kedinizin kısırlaştırılmış olup olmadığını (e/h) cinsinden giriniz:")
    if kisir == "e":
        mama_fiyat = KISIR_MAMA
        mama_turu = "Kısır Maması"
    else:
        mama_fiyat = YETISKIN_MAMA
        mama_turu = "Yetişkin Maması"

if 0 <= kedi_ay < 3:
    mama_miktari = round(kedi_agirlik * KG_YUZDE_0_3)
elif 4 <= kedi_ay <= 6:
    mama_miktari = round(kedi_agirlik * KG_YUZDE_4_6)
elif 7 <= kedi_ay <= 12:
    mama_miktari = round(kedi_agirlik * KG_YUZDE_7_12)
else:
    mama_miktari = round(kedi_agirlik * KG_YUZDE_13)

toplam_mama_masraf = mama_miktari * 30 * mama_fiyat/1000

print("Almanız gereken kedi maması tipi:", mama_turu)
print("Kedinize vermeniz gereken günlük mama miktarı", round(mama_miktari), "gr")
print("Aylık kedi maması masrafınız: {:.2f} TL".format(toplam_mama_masraf))
