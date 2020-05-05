# -*- coding: utf-8 -*-

#---Заполнение файла списка KKS кодов, с контролем наличия в списке (20-02-2020 v.1)

def init():
	while 1:
		print("Имя файла для заполнения (vlv.txt, pump.txt,..):")
		filename = input()		
		print("Префикс (040T25):")
		prefix = input()
		print("Тип элементов (S,L):")
		type = input()
		print("---")
		print("{0}xxx{1}xx".format(prefix,type))
		print("Все верно? (Y/N)")
		Y = input()
		if Y=='Y' or Y=='y':
			return filename, prefix, type

filename, prefix, type = init()

print("---")
print("Начинаем внесение данных в файл {0}:".format(filename))

kkslist = list()

try:
  myfile = open(filename)
except IOError as e:
  print ("---Файл не найден")
else:
  with myfile:
    kkslist = myfile.read().splitlines()

print (kkslist)
print (">>>")

while 1:
  kks1 = input("{0}".format(prefix))

  if not kks1:
    N = input("{0}{1} (Enter=YES/N=no)?".format(prefix, lastkks1))
    kks1 = lastkks1
    if N=='N' or N=='n':
      kks1 = input("{0}".format(prefix))
  else:
    lastkks1 = kks1

  kks2 = ""
  if type:
    kks2 = input("{0}{1}{2}".format(prefix,kks1,type))    
  item = "{0}{1}{2}{3}".format(prefix,kks1,type,kks2)
  print ("---"+item)
  if not item in kkslist:
    kkslist.append(item)
    print("-+-Добавлено")
    with open(filename, "a") as myfile:
      myfile.write(item+"\n")
 
  else:
    print ("-!-Уже есть в списке")