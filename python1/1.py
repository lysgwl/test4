# -*- coding: UTF-8 -*-
import os
import re
import sys
import time
import random
import string

import ConfigParser


'''
#part1:
def main():
	print ("this is a test!")

#Make a script both importable and executable
#让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
if __name__=='__main__':
	main()
'''

'''
#part2:
a = 123 #10-2
b = "the value is:{result}".format(result=a)
print (b)
'''

'''
def part2_test1(param1):
	n1 = param1 + 1;
	n2 = n1 + 1;
	n3 = n2 + 1;
	print ("value : %d,%d,%d"%(n1,n2,n3))
	return n1,n2,n3,'123'

a1 = part2_test1(101)
print (a1)	
'''

'''
def part2_test2():
	str1 = "this is a test!"
	s1 = str1.split(' ')	
	print (s1)

	strArray = ['test1', "test2", "test3"]
	sorted(strArray)

	print ("Array first value:%s" % strArray.pop(0))
	print ("Array last value:%s" % strArray.pop(-1))

	print ("Please Input Value1: ") 
	nValue1 = 100 #int (raw_input(">"))
	nValue2 = 101
	nValue3 = 102
	if nValue1 < nValue2:
		print ("nValue1:%d < nValue2:%d" % (nValue1, nValue2))
	elif nValue1 < nValue3:
		print ("nValue1:%d < nValue3:%d" % (nValue1, nValue3))
	else:
		print ("nValue1:%d > nValue2:%d, nValue3:%d" % (nValue1, nValue2, nValue3))
	
	nArray1 = [1, 2, 3]
	for number in nArray1:
		print ("nArray count is:%d" % number)

	strArray1 = ['test1', 'test2', 'test3']
	for str1 in strArray1:
		print ("strArray type is:%s" % str1)

	sArray1 = [1, 'test1', 2, 'test2', 3, 'test3']
	for nIndex in sArray1:
		print ("sArray1 type is:%r" % nIndex)

	elements = []
	for nIndex in range(0, 10):
		elements.append(nIndex)
	for nIndex in elements:
		print ("elements array is:%d" % nIndex)
part2_test2()

#def part2_test3():
'''

'''
#python  配置文件解析
#part3:
def dirlist(dirpath, filelist):
	list = os.listdir(dirpath)	
	
	for filename in list:
		filepath = os.path.join(dirpath, filename)
		if os.path.isdir(filepath):
			dirlist(filepath, filelist)
		else:
			if os.path.isfile(filepath):
				filelist.append(filepath)
			
	return 	filelist
	
def findstr(filepath, keyword):
	global everyline
	right=[]
	
	fp = open(filepath, 'r')
	for everyline in fp:
		if re.search(keyword, everyline, re.I):
			right.append(filename)
			break
			
	return right

def parseconfig():
	cf = ConfigParser.ConfigParser()	
	
def part3_test1():
	abs_path_name = os.path.dirname(__file__)
	cur_path_name = os.path.abspath(abs_path_name)
	file_path_name = cur_path_name + "\\t1"
	
	if not os.path.exists(file_path_name):
		os.makedirs(file_path_name)
		
	for nIndex in range(1,15):
		file_name = "file%d.txt"%nIndex
		file_path = "%s\\%s"%(file_path_name,file_name)
		
		if not os.path.exists(file_path):
			f = open(file_path, 'w')
			if(f):
				f.close()
				
	s = dirlist(file_path_name, [])

part3_test1()		

#part4:		
class Cat(object):
	def __init__(self):
		self.name = name
	def play():
		print ("I Like play")

class BossCat(Cat):
	def play(ball):
		print ("I Like play %s" %ball)
			
class Person():	
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	
	def get_name(self):
		return self.__name
		
	def set_name(self,name):
		self.__name = name

class EmailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email	

class Student(object):
	def birth(self):
		return self._birth
	def birth(self,value):
		self._birth = value
	def age(self):
		return 2014-self._birth
'''