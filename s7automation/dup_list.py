# -*- coding: utf-8 -*-

#---Проверка дубликатов KKS кодов в списке

import os
import re

from itertools import groupby

print("Содержимое папки:")
files = os.listdir()
print (files) 

print("Имя файла для чтения:")
filename1 = input()		

#print("Имя файла для записи:")
filename2 = "uniq_"+filename1

try:
  myfile = open(filename1)
except IOError as e:
  print ("---Файл не найден")
else:
  with myfile:
    linelist = myfile.read().splitlines()


uniqlist = [el for el, _ in groupby(linelist)]

for kks in uniqlist:
    with open(filename2, "a") as myfile2:
        myfile2.write(kks+"\n")


print("---Файл сохранен.")