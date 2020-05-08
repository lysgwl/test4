# -*- coding: UTF-8 -*-

import os
import sys

import re
import csv

def readCsvTup(strFilePath):
    with open(strFilePath, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        data = [tuple(i) for i in reader]
        return data

def writeCsvTup(strFilePath, dataList):
    with open(strFilePath, 'wb', encoding="utf-8") as f:
        return

def parseTupData(strData):
    if not isinstance(strData, str):
        return

    line = re.sub('[\r\n]', '', strData)
    lineList = line.split(';')
    if len(lineList) != 3:
        return

    userData = lineList[2]
    if userData.strip() == '':
        return

    userList = userData.split(' ')
    if len(userList) != 3:
        userName = lineList[0]
    else:
        userData = userList[1]
        pos = userData.find('+')
        if pos == -1:
            userName = lineList[0]
        else:
            userName = userData[pos:len(userData)]

    dataList = []
    dataList.append(lineList[0])
    dataList.append(lineList[1])
    dataList.append(userName)
    return dataList

def compareList(curList, prevList):
    if len(curList) == 0 or len(prevList) == 0:
        return

def getTupList(dataList):
    prevList = []

    for i in dataList:
        if len(i) == 0:
            continue
        else:
            data = i[0]
            curList = parseTupData(data)
            if len(curList) == 0:
                continue

            if len(prevList) != 0:
                compareList(curList, prevList)

            prevList.clear()
            prevList = list(curList)

def setTupList(mode, startCaller, startCallee, endCaller, endCallee):
    if len(startCaller) == 0 or len(startCallee) == 0:
        return

    if len(endCaller) == 0 or len(endCallee) == 0:
        return

    startCallerNum = int(startCaller)
    startCalleeNUm = int(startCallee)

    endCallerNum = int(endCaller)
    endCalleeNum = int(endCallee)

    if startCallerNum > endCallerNum:
        listLen = startCallerNum - endCallerNum
    else:
        listLen = endCallerNum - startCallerNum

    dataList = []
    listLen = listLen + 1

    #for i in range(listLen):

def test1():
    setTupList(1, '16188880001', '16188885001', '16188880020', '16188885020')

def test2():
    data = readCsvTup('1.csv')
    if len(data) == 0:
        return

    #getTupList(data)

def main():
    #test1()
    test2()

if __name__ == "__main__" :
	main()