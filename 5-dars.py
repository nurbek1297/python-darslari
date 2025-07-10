# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 19:10:35 2025

@author: User
"""

# 11-dars
# elif aks holda agar
hafta_kuni = int(input("Qaysi kuni kursiz bor: \n>>>>"))
if hafta_kuni <= 1:
    kun = "Dushanba kuni ekan"
elif hafta_kuni <= 2:
    kun = "Seshanba kuni ekan"
elif hafta_kuni <= 3:
    kun = "Chorshanba kuni ekan"
elif hafta_kuni <= 4:
    kun = "Payshanba kuni ekan"
elif hafta_kuni <= 5:
    kun = "Juma kuni ekan"
elif hafta_kuni <=6:
    kun = "Shanba kuni ekan"
elif hafta_kuni <=7:
    kun = "Dam olish kuni ekan"
else:
    kun = "Xato yozdingiz bunday kun yo'q "
    
print(kun)
     
#  or yoki  deb tarjima qilinadi
maktab = int(input("Siz qaysi maktabda o'qiysiz faqat raqamini yozing:\n>>>"))
if maktab == 15 or maktab == 81 or maktab == 16 :
    joy = 'Bu maktab "Moskvada" '
elif maktab == 34:
    joy = 'Bu maktab "Qovoqda" '
elif maktab ==88:
    joy = 'Bu maktab "Chinobodda" '
else:
    joy  = 'Bu maktab haqida ma\'lumotga ega emasman'
print(joy)

# and va deb tarjima qilinadi
soat = int(input('Soat nechchi:\n>>> '))
_soat = str(input("Qachongi \n>>>"))
if soat ==2 and _soat.lower() == 'abetki':
    print("Cho'milgani boraylik")
else:
    print("Uxla")



#  Boolean  mantiqiy ma'lumot turi
osh = 25000
choy = False
salat = True

if choy and salat :
    osh = osh + 10000
elif choy or salat :
    osh = osh + 20000
    
print(f"Siz {osh} tulov qilasiz")



shot = 50000
choy = True
assorti = False
tabaka = False
non  = False
xizmat_xaqi = True  

if choy:
    print('choy 3000')
    shot = shot + 3000
    
if assorti :
    print('assorti 8000')
    shot = shot + 8000
    
if tabaka :
    print('tabaka 65000')
    shot = shot + 65000
    
if non :
    print('non 5000')
    shot = shot + 5000
    
if xizmat_xaqi :
    print('xizmat xaqi 20000')
    shot = shot + 20000
    
    
print( f" siz {shot} tulov qilasiz" )


# in bu malum bir elementni ro'yxat ichida bor yo'qligini tekshiradi  not in buni aksi
menu = ['somsa' , 'shashlik' , 'shurbo' , 'pichak' , 'manti' , 'barak']
buyurtma = input('Nima ovqat buyurtma qilasiz: \n>>>  ')
if buyurtma.lower() in menu :
    print('hozir olib kelaman')
else:
    print('bunday ovqat yuq')
    
    
menu = ['somsa' , 'shashlik' , 'shurbo' , 'pichak' , 'manti' , 'barak']
pochta = []
pochta.append(input('nima yeyishni hohlaysiz'))
if pochta:
    print('hozir keladi')
else:
    print('tur yuqol restorandan ho\'kiz')
for taom in pochta:
    if taom in menu:
        print(f"ha bizda {taom} bor")
    else:
        print(f"yuq bizda {taom} yuq")
        
        
        
        
        
        
        
        
    
    
    
# 12-dars
# Erorr ya'ni Xatolar
# SintaxErorr dasturlash qoidalariga amal qilmasdan yozilgan kod
# EOF xatoligi biror funksiyada qavslar  yoplimay qolip ketgan
# EOL qator oxirida xatolik bor


# RantimeErorr lar juda ko'p 6ta eng asosiy xatolar bular
# EndintationErorr  kutilmagan joy tashab yozish xatoligi
# for siklini badalida joy tashlab yozish kerak tab tugmasida bitta joy tashlash tavsiya etiladi
# typeErorr ma'lumot turi ustida bajarib bo'lmadigan amalni bajarsak xato chiqadi
# nameErorr  o'zgaruvchi yoki fuksiya nomini xato yozish ntijasida kelib chiqadi
# valueErorr noto'g'ri qiymat natijasida kelib chiqadi
# indexErorr ro'yxat ichidagi elementlarga noto'g'ri index bilan murojat qilish 
# zeroDivisionErorr sonni nolga bo'lish xatoligi  



# Mantiqiy xatolar dasturchi yo'l quygan xatolar
    










import ("io","strconv")
	
	


type mustWriter struct {
	io.Writer
}

func (w mustWriter) Write(p []byte) (int, error) {
	n, err := w.Writer.Write(p)
	if err != nil {
		panic(err)
	}
	return n, nil
}

func mustParseInt(str string, base, bits int) int64 {
	i, err := strconv.ParseInt(str, base, bits)
	if err != nil {
		panic(err)
	}
	return i
}

func mustParseUint(str string, base, bits int) uint64 {
	i, err := strconv.ParseUint(str, base, bits)
	if err != nil {
		panic(err)
	}
	return i
}

func mustParseFloat(str string, bits int) float64 {
	i, err := strconv.ParseFloat(str, bits)
	if err != nil {
		panic(err)
	}
	return i
}

func mustParseBool(str string) bool {
	i, err := strconv.ParseBool(str)
	if err != nil {
		panic(err)
	}
	return i
}
























