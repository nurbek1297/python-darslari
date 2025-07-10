# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 19:34:37 2025

@author: User
"""

# 6-dars
# sonlar ustida amallar
# integer butun son
a = 56

# float o'nlik son
b = 2.3

# type funksiyasi o'garuvchila turni aniqlab beradi
aholi_soni = 7_889_789_456
print(aholi_soni)


# pythonda bir qatorga bir nechta o'zgaruvchi yozish mumkin
x,y,z = 23 , 25 , -2.56


# pythonda o'zgarmas yo'q lekn pythin dasturchilari katta harflar bilan yozilgan o'zgaruvchini o'zgartirmaydi
# Pythonda funksiyalar ma'lum bir ma'lumotni olib uni ko'rinishini o'zgartirib beradi





# int() funksiyasi ichidagi ma'lumotni butun son qilib beradi
# float() funksiyasi ichidagi ma'lumotni o'nlik son qilib beradi qilib beradi
# str() funksiyasi ichidagi ma'lumotni matn qilib  qilib beradi




# 7-dars
# list bu ro'yxat bitta o'zgaruvchiga bir neachta matn  datatype yozamiz
mevalar = ['anjir',58,2.6,'anor','olma','uzum']
print(mevalar)
print('birinchi meva:' , mevalar[0].upper())
print('ikkinchi meva:' , mevalar[2])
# -  ishorasi oxiridan sanab keladi
print(mevalar[-3])







# [] bo'sh ro'yxat bu ro'yxat foydalanuvchi ma'lumot kirgizganda kerak bo'ladi
ismlar = []

narhlar = [1200000, 122222222222,5455555555,2333]
print(narhlar[2]-8955555555555)



#  append() methodi ro'xatni oxiriga yangi sonlar qo'shadi
mevalar.append('Qovun')
print(mevalar)


#  insert() methodi hohlagan joyga yangi ro'yxat qo'shadi birinchi index keyin ro'yxat yoziladi

narhlar.insert(3, 'bu uchinchi harh edi')
print(narhlar)

cars = []
cars.append(input('moshinalar nomi yoz\n>>>>'))
print(cars)


# del() malum keraksis elementni o'chiradi ro'yhat ichidan
# del cars[5]

# remove() methodi hohlagan elementi faqat birinchi uchraganini nomi bilan o'chirish imkonini beradi

# cars.remove('monza')

#  pop() hohlagan elemantni sug'urib oladi index berilmasa oxiridagi elementni oladi
bozorlik = ['un','piyoz','olma''kartoshka','guruch']
bozorlik = bozorlik.pop(1)




#  8-dars

#  sort() methodi ro'yxatni alifbo ketma-ketligida qilib beradi sonlarda ham ishlaydi
logo_football = ['barselona', 'atletico', 'real madrid','arsenal','manchester city']
# reverse=True argumenti teskari alifbo qilib beradi
logo_football.sort(reverse=True)
print(logo_football)


#  sorted() methodi faqat ko'rinishini alifbo tartibida yozib beradi sonlarda ham ishlaydi
sorted(logo_football)

#  reverse() faqat ro'yxatni teskari qilib beradi 
logo_football.reverse()



# len() methodi ro'yxat uzunligini aniqlab beradi
len(logo_football)




#  range() methodi aytilgan sonlarni ro'yxat qiladi
sonlar = list(range(1,1000,5)) # uchinchi raqam qadamni bildiradi
print(sonlar[89:150])


# max() eng katta qiymatni topadi min() eng kichinasini topadi sum() hammasini qo'shadi
min_qiymat = min(sonlar)
max_qiymat =  max(sonlar)
jami = sum(sonlar)
print(f"{max_qiymat} , {min_qiymat} ,{jami}")

my_number = sonlar[:]
print(my_number.remove(996))



#  TUPLE o'zgarmas ro'yxat bu () yoziladi
sabzi =   ('urugi','guli', 'mevasi', 'tomiri')
sabzi = list(sabzi)
sabzi.append('donak')
sabzi = tuple(sabzi)
print(sabzi)
































