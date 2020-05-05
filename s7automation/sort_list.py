# -*- coding: utf-8 -*-

#---Сортировка списка KKS кодов по символу объекта F,P,T

#---версия 2.0

import os
import re

print("Содержимое папки:")
files = os.listdir()
print (files) 

print("Имя файла для чтения:")
filename1 = input()		

#print("Имя файла для записи:")
filename2 = "srt_"+filename1
filename3 = "srterr_"+filename1

linelist2d = []

try:
  myfile = open(filename1)
except IOError as e:
  print ("---Файл не найден")
else:
  with myfile:
    linelist = myfile.read().splitlines()
    
errlist = list()

errors=0     
cnt=0
for line in linelist:
  match = re.search(r"\D(\d)+$", line) 
  try:
    match2 = re.search(r"\D",match[0])
    linelist2d.append([])
    linelist2d[cnt].append(line)
    linelist2d[cnt].append(match[0])
    cnt=cnt+1
  except Exception:
    errors=errors+1
    errlist.append(line)
    print(line)

linelist2d.sort(key=lambda x: x[1])

for line in linelist2d:
  for kks in line:
  	match = re.search(r"\d\d\d\D(\d)+\D(\d)+\S", kks)
  	if match:
  		#print(match[0])
  		with open(filename2, "a") as myfile2:
  			myfile2.write(match[0]+"\r\n")


print("---Ошибок обработки {0}".format(errors))

for line in errlist:
  with open(filename3, "a") as myfile3:
    myfile3.write(line+"\r\n")
