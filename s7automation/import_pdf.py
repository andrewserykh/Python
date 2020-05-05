# -*- coding: utf-8 -*-

#---Создание списка KKS из вырезанного текстового файла таблицы В1 (20-02-2020 v.1)
#1. Давление 040T16000P01       040T16000P01XQ01 
#2. Температура 040T16000T02  040T16000T02XQ01 
#3. Температура 040T16000T03  040T16000T03XQ01 

import re
import os

print("Содержимое папки:")
files = os.listdir()
print (files) 

print("Имя файла для чтения:")
filename1 = input()		

print("Имя файла для записи:")
filename2 = input()		

try:
  myfile = open(filename1)
except IOError as e:
  print ("---Файл не найден")
else:
  with myfile:
    linelist = myfile.read().splitlines()

for line in linelist:
  match = re.search(r"\d\d\d\D(\d)+\D(\d)+\S", line) 
  print(match[0] if match else "---Не найдено")
  with open(filename2, "a") as myfile2:
    myfile2.write(match[0]+"\n")
