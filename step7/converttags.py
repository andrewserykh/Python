#--- Обработчик таблицы тегов WinCC 7.4		05.05.2020
#     -  замена структурных тегов на "короткие" имена
#     -  удаление неиспользуемых в АСОДУ тегов

import sys, argparse, os, re

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--src')
    parser.add_argument ('--dest')
    parser.add_argument ('--plc')    
    return parser
 
print ("WinCC 7.4 Tag Table Converter v.2\n")
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.src and namespace.dest and namespace.plc:
      filesrc = namespace.src
      filedest = namespace.dest
      plcname = namespace.plc
      
    else:
      print (" * usage:\n[thisfile.py] --src SourceName --dest DestinationName --plc PlcNewName \n")
      sys.exit()
 
print (" - Opening Taglist {}".format(filesrc))

try:
  with open(filesrc, 'rb') as source:
    contents = source.read()
except IOError as e:
  print (" ! File not found")
  sys.exit

contents = contents.decode('utf-16')

lines = contents.splitlines()
linescntsrc = len(lines)

#Поиск S7 Connection для получения имени PLC
Chapter = ""
ConnectionName = ""
linesDest = list()


#Перебор файла построчно
for line in lines:

  del_this_line = False
  
  #Раздел DmConnection
  match = re.search(r'DmConnection',line)
  if match:
    Chapter = "DmConnection"
    print (" > DmConnection")    

  #Раздел DmStructtype
  match = re.search(r'DmStructtype',line)
  if match:
    Chapter = "DmStructtype"
    print (" > DmStructtype")

  #Раздел DmStructtypeElement
  match = re.search(r'DmStructtypeElement',line)
  if match:
    Chapter = "DmStructtypeElement"
    print (" > DmStructtypeElement")

  #Раздел DmStructtag
  match = re.search(r'DmStructtag',line)
  if match:
    Chapter = "DmStructtag"
    print (" > DmStructtag")

  #Раздел DmTag
  match = re.search(r'DmTag',line)
  if match:
    Chapter = "DmTag"
    print (" > DmTag")
    
  #Поиск и замена в S7 Connection  
  match = re.search(r'SIMATIC S7 Protocol Suite', line) 
  if match:
    oldConnectionLine = line
    ConnectionName = line.partition('SIMATIC S7 Protocol Suite')[0]
    match = re.search(r'\D\d', ConnectionName) 
    if match:
      ConnectionName =  match[0]
      print (" - Connection ",ConnectionName," -> ", plcname)    
    line = line.replace(ConnectionName,plcname,1)

  #Замена S7 различных разделах
  if Chapter == "DmStructtype":
    line = line.replace(ConnectionName,plcname,1)

  if Chapter == "DmStructtypeElement":
    line = line.replace(ConnectionName+"/",plcname+"/",1)
    
    #фильтрация неиспользуемых в АСОДУ тегов
    match = re.search(r'^[a-zA-Z0-9#_]{2,}\s\d\s\w{2,}', line)
    if match:
      match = re.search(r'^[a-zA-Z0-9#_]{2,}', match[0])
      if match:
        del_this_line = True
        if match[0]=="VALUE":
          del_this_line = False
        elif match[0]=="OUT":
          del_this_line = False
        elif match[0]=="EOUT":
          del_this_line = False
        elif match[0]=="DISPLAY":
          del_this_line = False
        elif match[0]=="WARNG_H":
          del_this_line = False
        elif match[0]=="WARNG_L":
          del_this_line = False
        elif match[0]=="ALARM_H":
          del_this_line = False
        elif match[0]=="ALARM_L":
          del_this_line = False
        elif match[0]=="FAULT":
          del_this_line = False    

  if Chapter == "DmStructtag":
    line = line.replace(ConnectionName+"/",plcname+"/",2)
    line = line.replace("	"+ConnectionName+"	","	"+plcname+"	",1)
    
    #поиск и удаление название CFC схемы
    line = re.sub(r'^'+plcname+'/\w{2,}', plcname, line)

  if Chapter == "DmTag":
    line = line.replace(ConnectionName+"/",plcname+"/",1)
    line = line.replace("	"+ConnectionName+"	","	"+plcname+"	",1)

    #поиск и удаление название CFC схемы
    line = re.sub(r'^'+plcname+'/\w{2,}', plcname, line)
  
    #фильтрация неиспользуемых в АСОДУ тегов
    match = re.search(r'^[a-zA-Z0-9#_]{2,}/[a-zA-Z0-9#_]{2,}.[a-zA-Z0-9#_]{2,}', line)
    if match:
      match = re.search(r'[.][a-zA-Z0-9#_]{2,}', match[0])
      if match:
        del_this_line = True
        if match[0]==".VALUE":
          del_this_line = False
        elif match[0]==".OUT":
          del_this_line = False
        elif match[0]==".EOUT":
          del_this_line = False
        elif match[0]==".DISPLAY":
          del_this_line = False
        elif match[0]==".WARNG_H":
          del_this_line = False
        elif match[0]==".WARNG_L":
          del_this_line = False
        elif match[0]==".ALARM_H":
          del_this_line = False
        elif match[0]==".ALARM_L":
          del_this_line = False
        elif match[0]==".FAULT":
          del_this_line = False    
    
  #Запись изменений в новый список
  if not(del_this_line):
    linesDest.append(line)

#Формирование выходного файла из списка lines
destContent = ""
for line in linesDest:
	destContent = destContent + line + "\r\n"
print (" - Lines in src/dest: ",linescntsrc," -> ",len(destContent.splitlines()))

with open(filedest, 'w+b') as destination:
  destination.write(destContent.encode('utf-16'))

print (" - Destination file saved\nDone\n")
