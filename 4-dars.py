# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 17:28:02 2025

@author: User
"""

#  9-dars

# for=uchun ayalana skili bo'ladi
osimliklar = ['kenza','mosh','tikan','somon','hashak']
for osimlik in osimliklar:
   print( 'mollar', osimlik , 'yeydi')
   print( 'mollar', osimlik , 'yemaydi')
# yonga joy tashlanmasa skil ichidan chiqib ketadi


sonlar = [23 , 36 , 89 , 87 , 56 , 25 , 45 , 83]
for son in sonlar:
   print(f"{son} ning kubi {son**3} ga teng")



sonlar = list(range(56))
sonlar_kubi = []
for son in sonlar:
    sonlar_kubi.append(son**3)
    

print(sonlar)
print(sonlar_kubi)


#  yakuniy misol
dostlar = []
print("6 ta eng yaqin do'tingiz kim")
for n in range(6):
    dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting \n>>>"))
    dostlar.sort()
print(dostlar)



# 10-dars
# if agar deb tarjima qilinadi

osimliklar = ['kenza','mosh','tikan','somon','hashak']
for osimlik in osimliklar:
      if osimlik == 'hashak':
          print(osimlik.upper())
#  else aks holda          
      else:
        print(osimlik.title())
        
# mantlarni bitta ko'rinishda keltirib olish kerak
# != teng emasmi degan belgi 


ism = input('Isming nima \n>>>>' )
if ism.lower() != 'nurbek':
    print(f"Uzur {ism.title()} men Nurbekni kutayapman ")
else:
    print(f"Salom {ism.title()}")
    





javob = float(input('56**2 nechaga teng:\t'))
if javob !=3136:
    print('ikkichi javobing xato')
else:
    print('yaxshi uka o\'sish bor')
    
# >= katta yoki teng <=kichik yoki teng
yosh = int(input('yoshingiz nechchida:\t'))
if yosh >= 18:
    print("EEE ammam qatorimisiz")
else:
    print('Hali gudak ekansan chop qumingni uyna')
    
login = input('Yangi login tanlang:\t')
if len(login)<=5 :
    print('Bu parol juda qisqa')


yosh = int(input("Tug\'ilgan yilingizni kiriting:\t"))
if 2025-yosh <18 :
    print(f"Yoshingiz {2025-yosh} da  sizga kirish mumkin emas")
else:
    print("xush kelibsiz")

































