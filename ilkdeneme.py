matematik = input('matematik : ')
turkce = input('turkce : ')
kimya = input('kimya : ')
fizik = input('fizik : ')
biyoloji = input('biyoloji : ')
tarih = input('tarih : ')
toplam=(float(matematik)+float(turkce)+float(kimya)+float(fizik)+float(biyoloji)+float(tarih)*25)/30
print("Toplam :{0} ".format(toplam))
if(toplam<50):
  print("Sınıfta kaldınız")
else:
  import androidhelper
droid = androidhelper.Android()
droid.ttsSpeak("sınıfı geçtin")
import androidhelper
droid = androidhelper.Android()
droid.makeToast('Sonuç bulundu')