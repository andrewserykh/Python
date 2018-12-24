
# -*- coding: utf-8 -*-

from docx import Document
import re

document = Document('/Users/andrew.serykh/Python/v1.docx')


def table_automation(table):
    LSU = 15 #отделение

    for row in table.rows:
        for count, cells in enumerate(row.cells):
            row_tmp = cells.text

#        if len(row.cells)>2:
#            row_name = row.cells[0].text
#            row_kks = row.cells[1].text
#            row_adr = row.cells[2].text
# 040T15228P01XQ01
            patternS = re.compile(r"""
            (\d{3})
            T
            (\d+)
            S
            (\d+)
            /
            (\d+)*
            """, re.I | re.VERBOSE)
            patternL = re.compile(r"""
            (\d{3})
            T
            (\d+)
            L
            (\d+)*
            """, re.I | re.VERBOSE)

            if len(row_tmp)<=20:
                if patternL.search(row_tmp):
                    kks = patternL.search(row_tmp)
                    try:
                        next_cell = re.sub("^\s+|\n|\r|\s+$", '', row.cells[count+1].text)
                    except:
                        next_cell = ""
                    try:
                        prev_cell = re.sub("^\s+|\n|\r|\s+$", '', row.cells[count-1].text)
                    except:
                        prev_cell = ""

                    postfix="_A"
                    if prev_cell.find(u"отключён")>0: postfix="_I"
                    if prev_cell.find(u"нерабочем")>0: postfix="_H"
                    if prev_cell.find(u"открытие")>0: postfix="_C"
                    if prev_cell.find(u"закрытие")>0: postfix="_D"
                    if prev_cell.find(u"температура")>0: postfix="_T"
                    if prev_cell.find(u"не открыт")>0: postfix="_A"
                    if prev_cell.find(u"не закрыт")>0: postfix="_B"
                    if prev_cell.find(u"открытия")>0: postfix="_E"
                    if prev_cell.find(u"закрытия")>0: postfix="_F"

                    if prev_cell.find(u"открыть")>0: postfix="_X"
                    if prev_cell.find(u"закрыть")>0: postfix="_Y"
                    kks = kks.group()
                    kks = kks.replace('/', '_')
                    kks = kks + postfix

                    DD0 = "0"
                    DD1 = "0"
                    DD2 = "0"
                    err=0
                    try:
                        match = re.search(r'-DD?([^.>]+)', next_cell) #1.
                        DD0 = match.group(1)
                        match = re.search(DD0+r'.?([^:>]+)', next_cell) #.10:
                        DD1 = match.group(1)
                        match = re.search(DD1+r':(\d+)', next_cell) #:14
                        DD2 = match.group(1)
                    except:
                        err=err+1


                    shift = 0
                    if (int(DD0)==1):
                        shift = 2
                    if (int(DD0)==2):
                        shift = 42
                    if (int(DD0)==3):
                        shift = 82
                    if (int(DD0)==4):
                        shift = 122
                    if (int(DD0)==5):
                        shift = 162
                    if (int(DD0)==6):
                        shift = 202
                    if (int(DD0)==9):
                        shift = 252
                    if (int(DD0)==10):
                        shift = 267
                    if (int(DD0)==405):
                        shift = 300

                    addr = 0
                    addrDD2 = 0
                    if (LSU==15):
                        if (int(DD2)>=2 and int(DD2)<=9):
                            addrDD2 = int(DD2)-2
                            shift = shift
                        if (int(DD2)>=12 and int(DD2)<=19):
                            addrDD2 = int(DD2)-12
                            shift = shift + 1
                        if (int(DD2)>=22 and int(DD2)<=29):
                            addrDD2 = int(DD2)-22
                            shift = shift + 2
                        if (int(DD2)>=32 and int(DD2)<=39):
                            addrDD2 = int(DD2)-32
                            shift = shift + 3
                        if (int(DD2)>=42 and int(DD2)<=49):
                            addrDD2 = int(DD2)-32
                            shift = shift + 4
                        if (int(DD2)>=52 and int(DD2)<=59):
                            addrDD2 = int(DD2)-32
                            shift = shift + 5


                        addr = shift + (int(DD1)-3)*4

                    if (LSU==22):
                        if (int(DD2)>=2 and int(DD2)<=9):
                            addrDD2 = int(DD2)-2
                            shift = shift
                        if (int(DD2)>=12 and int(DD2)<=19):
                            addrDD2 = int(DD2)-12
                            shift = shift + 1
                        if (int(DD2)>=22 and int(DD2)<=29):
                            addrDD2 = int(DD2)-22
                            shift = shift + 2
                        if (int(DD2)>=32 and int(DD2)<=39):
                            addrDD2 = int(DD2)-32
                            shift = shift + 3

                        addr = shift + (int(DD1)-3)*4

                    if postfix=="":
                        if (addr>0 and addrDD2>0):
                            print kks,"\t I \t",addr,".",addrDD2
                        #print "--",kks,"\t" ,next_cell, "\t '",prev_cell,"'"
                    else:
                        if (addr>0 and addrDD2>0):
                            print kks,"\t I \t",addr,".",addrDD2
                        #print "--",kks, "\t", next_cell
    return 0


count = 0
for table in document.tables:
    count += table_automation(table)
