import os

# dosyanın bulunduğu yol
dosya_yol = os.getcwd()+"\\"
print("Bulunduğun klasör :", dosya_yol)


# bilgisayar adını öğrenme
bilgisayar_adi = os.environ['COMPUTERNAME']
print("Bilgisayar adı: ", bilgisayar_adi)

# çıktıdosyasının adını oluştur
cikti_dosyasi_adi = bilgisayar_adi + ".txt"
print("Çıktı dosyası adı : " , cikti_dosyasi_adi)

# komutları dosyadan alma
komut_dosyasi = open("komut_dosyasi.txt","r")
kd = komut_dosyasi.readlines()
print("Çalıştırılacak komut : ", kd[0])
#print(kd)

#komut = kd[0]+" > "+os.getcwd()+"\\" + cikti_dosyasi_adi
k = str(kd[0]).strip()
komut = k + " > " + os.getcwd() + "\\" + cikti_dosyasi_adi

#komut2 = "netsh wlan show profiles > C:\\Users\\cllaks\\Desktop\\denemedosyasi.txt"
#print("komut2 nin değeri :",komut2)

# cmd komutunun çalıştırılması os.system("komut > dosyayol+dosya adı")
#os.system(kd[0]+" > "+dosya_yol+cikti_dosyasi_adi)
#os.system("netsh wlan show profiles > C:\\Users\\cllaks\\Desktop\\denemedosyasi.txt")
os.system(komut)


# ağ adını dosyadan alma
ag_liste = open(cikti_dosyasi_adi,"r")
al = ag_liste.readlines()
ag_liste.close()
# os.remove(cikti_dosyasi_adi)
print(al)

# Ağ ve şifre bilgilerini kayıt etmek için dict tanımlanıyor
sifreler ={}

# Kablosuz ağ isimlerini alma işlemleri
kablosuz_aglar = []
sayac = 0
for i in al:
    sayac += 1
    if sayac >= 10:
        b = str(i).strip()
        print("dosyadan alınan ağ adı : ", b)
        ters_ad = ""
        for ham_b in reversed(b):
            if ham_b != " ":
                ters_ad = ters_ad + ham_b
            else:
                break
        print(ters_ad)
        ag_adi = ""
        for ham_b in reversed(ters_ad):
            ag_adi = ag_adi + ham_b
        print(ag_adi)
        kablosuz_aglar.append(ag_adi)
        gecici_liste = {ag_adi:""}
        print("geçici liste  :",gecici_liste)
        sifreler.update(gecici_liste)
print(kablosuz_aglar)
print("şifreler listesi : ",sifreler)

# Dosyadan sifreyi alma
def sifre_oku(dosya_adi):
    sifre_dosyasi = open(dosya_adi,"r")
    bilgiler = sifre_dosyasi.readlines()
    sifre = ""
    print(bilgiler)
    for i in bilgiler:
        if "Key Content" in i:
            print(i)
            b = str(i).strip()
            print(b)
            ters_sifre = ""
            for ham_b in reversed(b):
                if ham_b != " ":
                    ters_sifre += ham_b
                else:
                    break
            print(ters_sifre)
            for ham_b in reversed(ters_sifre):
                sifre += ham_b
            print(sifre)
    sifre_dosyasi.close()
    os.remove(dosya_adi)
    return sifre
    

            
# Kablosuz ağ adını komut içerisine yerleştirme ve şifresini dosyasını alma

k1 = kd[1].strip()
print(k1)
j = 0
for i in kablosuz_aglar :
    k1 = k1.replace("WIRELES_ADI",kablosuz_aglar[j])
    print(k1)
    print(kablosuz_aglar[j])
    komut2 = k1 + " > " + os.getcwd() + "\\" + kablosuz_aglar[j] + ".txt"
    os.system(komut2)
    # sifre_oku fonksiyonu için eklenen kodlar
    dosya_adi = kablosuz_aglar[j]+".txt"
    sifre_neyse = sifre_oku(dosya_adi)
    gecici_sozluk = {i:sifre_neyse}
    sifreler.update(gecici_sozluk)
    # son
    k1 = k1.replace(kablosuz_aglar[j],"WIRELES_ADI")
    j += 1
    

# Şifreyi sözlüğe ekleme

print("Ağ ve şifrelereeeeeeeerrrrr: ", sifreler)

sifre_dosyasi = open("kayitli_sifreler.txt","a")
sifre_dosyasi.write("Bilgisayar Adı : " + bilgisayar_adi + '\n\n')
for k, v in sifreler.items():
    sifre_dosyasi.write(str(k) + ' >>> ' + str(v) + '\n\n')

sifre_dosyasi.close()

