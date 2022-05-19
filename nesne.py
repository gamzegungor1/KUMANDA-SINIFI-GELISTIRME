import random 

import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal= kanal

    def tv_ac(self):
         if(self.tv_durum == "Açık"):
             print("Televizyon zaten açık ")

         else:
            print("Televizyon açılıyor.")
            self.tv_durum = "Açık"
    def tv_kapat(self):
         if (self.tv_durum == "Kapalı"):
           print("Televizyon zaten kapalı ")

         else:
          print("Televizyon kapanıyor")
          self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi Azalt : '<'\nSesi Artır: '>'\nÇıkış: Exit") 

            if(cevap == "<"):
                if(self.tv_ses !=0):

                    self.tv_ses -=1
                    print("Ses:", self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses +=1 
                    print("Ses: ", self.tv_ses)
    

    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor.")
        time.sleep(2)
        

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")


    def rastgele_kanal(self):
      # randint rastgele sayı üretir.
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu an ki Kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi:  {}\nŞu an ki Kanal:  {}\n".format(self.tv_durum, self.tv_ses,self.kanal_listesi,self.kanal) 

kumanda = Kumanda()
print("""



TELEVİZYON UYGULAMASI


1.TV AÇ
2.TV KAPAT
3.SES AYARLARI
4.KANAL EKLE
5.KANAL SAYISINI ÖĞRENME
6.RASTGELE KANAL GEÇME
7.TELEVİZYON BİLGİLERİ

ÇIKIŞ YAPMAK İÇİN 'q' YA BASINIZ.




""")
 
while True:
    işlem = input("İşlemi Seçiniz:  ")

    if (işlem =="q"):
        print("Program Sonlandırılıyor....")
        break 
    elif(işlem == 1):
        kumanda.tv_ac()
        #print("Tv Açılıyor...")
    elif(işlem == 2):
        kumanda.tv_kapat()
    elif(işlem == 3):
        kumanda.ses_ayarları()
    elif(işlem ==4):

        kanal_isimleri = input("Kanal İsimlerini ',' ile ayırarak giriniz: ")
        kanal_listesi = kanal_isimleri.split(",")     

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem == 5 ):
        print("Kanal Sayısı :",len(kumanda))

    elif(işlem == 6) :
        kumanda.rastgele_kanal()

    elif(işlem== 7):
        print(kumanda)

    else:
        print("Geçersiz İşlem... Lütfen Geçerli İşlem Giriniz.")    

