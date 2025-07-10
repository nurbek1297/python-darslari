# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 19:20:24 2025

@author: User
"""

#  o'zgaruvchilar turli xil ma'lumotlarni saqlash uchun kompyuter hotirasidan ajratilgan joy
#  o'zgaruvchilar bu quti unga narsalar solib unga nom berib qo'yamiz
ism = 'Nurbek'
yosh = 17
print( ism,yosh)


#o'zgaruvchilarni nomini o'zgaritmay ichidagi ma'lumotni o'zgartirsa bo'ladi
ism = 'Temur'
yosh = 19
print(ism , yosh)

#  o'zgaruvchilarga chiroyli nom berish kerak
#  o'garuvchilarga son qiymat bersa ham bo'ladi

son = 56
son1 = 48
son2= (son+son1)**2
print(son2)


#  o'zgaruvchiga boshlanishi son bilan boshlanmaslik kerak
#  o'zgaruvchi o'rtasida bo'sh joy bo'lmasligi kerak uning o'rniga _ dan qo'yish kerak
#  o'zgaruvchi katta kichina harflar turlicha talqin qilinadi

#  Bu so'zlardan foydalanib bo'lmaydi
#  False               class               from                or
#  None                continue            global              pass
#  True                def                 if                  raise
#  and                 del                 import              return
#  as                  elif                in                  try
#  assert              else                is                  while
#  async               except              lambda              with
#  await               finally             nonlocal            yield
#  break               for                 not   




#  5-dars

#  Unicode barcha belgilar va classlar mavjud bo'lgan sayt

# '' bo'shliq vazifasini bajaradi
ism = 'Nurbek'
familiya = 'Tursunov'

print(ism+ '  '+ familiya)\
    
#  f'' string bu barcha stringlarni bitta joyga jamlash
ism_familiya = f"{ism} {familiya}"
print(ism_familiya)

#  \t uzun bo'shliq belgisi

print('hello \t world')


#  String methodlari. methodlar 'matn.method' ko'rinishida yoziladi 

#  UPPER hammasini katta harf qilib beradi
print(ism_familiya.upper())

#  lower hamma harfni kichkina qilib beradi
print(ism_familiya.lower())

# Title hamma so'zni birinchi harfini katta qilib beradi
print(ism_familiya.title())


#   Capitalize so'zni faqat engbirinchi harfini katta qilib beradi
print(ism_familiya.capitalize())

# lstrip chap tarafdagi rstrip o'ng tarafdagi bo'shliqni olib tashlaydi
meva = '       olma         '
print(meva.lstrip().rstrip())

# strip ikki tomondan ham bo'shliqni olib tashlaydi
print(meva.strip())


# INPUT funksiyasi foydalanuvchidan ma'lumot olishda ishlatiladi

viloyat = input('Qaysi viloyatdansan?\n>>>>')
print('Men Toshkentlikman'+'   '+viloyat.capitalize()+'    '+'tanishganimdan xursandman')

























