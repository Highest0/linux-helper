import os
print("\033[94m")
print('''
 
           _				Selam! Ben Erzurumlu Linux Kurdu.
        / \      _-'			Bu Linux yolculuğunda sana yardımcı olmak için buradayım.
      _/|  \-''- _ /			Lütfen yapmak istediğin işlemi belirt.
 __-' { |          \			
     /              \			1-) Dosya Kopyala
     /       "o.  |o }			2-) Dizin Oluştur
     |            \ ;			3-) Dosya Sil
                   ',			4-) Dosya Taşı
        \_         __\			5-) Dosya Oluştur	
          ''-_    \.//			6-) Yazı Dosyası Oku
            / '-____'			7-) Zip İşlemleri	
           /				8-) Paket Yükle
         _'				9-) Sistem Bilgileri
       _-'

''')
asistansecenek = input("Seçim Belirtiniz. ")

if(asistansecenek=="1"):
	dosya = input("Dosya yolu belirtiniz > ")
	hedef = input("Hedef yolu belirtiniz >")
	os.system("cp "+dosya+" "+hedef)

elif(asistansecenek=="2"):
	dosya = input("Dizin adı giriniz. > ")
	os.system("mkdir "+dosya)
elif(asistansecenek=="3"):
	dosya = input("Dosya yolu belirtiniz. > ")
	os.system("rm -rf "+dosya)
elif(asistansecenek=="4"):
	dosya = input("Dosya yolu belirtiniz. > ")
	hedef = input("Hedef yolu belirtiniz. >")
	os.system("mv "+dosya+" "+hedef)
elif(asistansecenek=="5"):
	dosya = input("Dosya Adını uzantısı ile beraber belirtiniz. > ")
	os.system("touch "+dosya)
elif(asistansecenek=="6"):
	dosya = input("Dosya yolu belirtiniz. > ")
	os.system("cat "+dosya)
elif(asistansecenek=="7"):
	os.system("apt install zip unzip")
	print(''' 

1-) Dosya Sıkıştır

2-) Sıkıştırılmış Dosyayı Çıkar

	''')
	zip = input("Seçiminizi Yapını.z > ")
	if(zip=="1"):
		dosya = input("Oluşacak zip adı giriniz > ")
		hedef = input("Ziplenecek dosyayı belirtiniz (uzantı ile) >")
		os.system("zip -r "+dosya+".zip "+hedef)

	elif(zip=="2"):
		dosya = input("Çıkartılacak Dosya Yolu > ")
		os.system("unzip "+dosya)		


elif(asistansecenek=="8"):
	print("Eğer hata alıyorsanız sudo kullanmayı deneyin eğer root iseniz 'h' tuşuna basınız.")
	root = input("Kök kullanıcıya geçiş yapmak ister misiniz? (e/h) ")
	if(root=="e"):
		os.system("sudo su")
	elif(root=="E"):
		os.system("sudo su")

	elif(root=="h"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
	elif(root=="H"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
elif(asistansecenek=="9"):
	print("//--Sistem bilgisini görmek için root olmanız gerekmektedir--\\")
	os.system("sudo apt install neofetch")
	os.system("neofetch")