# -*- coding: UTF-8 -*-

import os
import re
import sys
import time
import random
import string

#import ConfigParser

def part_test1() :
	def param_test(param) :
		a = "value is :{result}".format(result=param);
		b = param;
		return a,b,'123'
		
	def array_test() :
		a = "this is a test!"
		a1 = a.split(' ')
		print(a1)
		
		a2 = ['test1', 'test2', 'test3']
		sorted(a2)
		
		print("array first value:%s"%a2.pop(0))
		print("array last value:%s"%a2.pop(-1))
		
		b1 = int(input("value1:>"))
		b2 = int(input("value2:>"))
		if b1 < b2 :
			print("value1:%d < value2:%d"%(b1, b2))
		else :
			print("value1:%d, value2:%d"%(b1, b2))
			
		b = [1, 2, 3]
		for index in b :
			print("array index:%r"%(index))
			
		b1 = []
		for index in range(0, 10) :
			b1.append(index)
			print("array value:%d"%index)
		
	a1 = param_test(101)
	print(a1)
	
	array_test()
	
def part_test2() :
	def dirlist(dirpath, filelist) :
		list = os.listdir(dirpath)	
		for filename in list :
			filepath = os.path.join(dirpath, filename)
			if os.path.isdir(filepath):
				dirlist(filepath, filelist)
			else:
				if os.path.isfile(filepath):
					filelist.append(filepath)
		return 	filelist
	
	def findstr(filepath, keyword) :
		global everyline
		right=[]
		fp = open(filepath, 'r')
		for everyline in fp:
			if re.search(keyword, everyline, re.I) :
				right.append(filename)
				break	
		return right
		
	abs_path_name = os.path.dirname(__file__)
	cur_path_name = os.path.abspath(abs_path_name)
	file_path_name = cur_path_name + "\\t1"
	
	if not os.path.exists(file_path_name):
		os.makedirs(file_path_name)
		
	for nIndex in range(1,15) :
		file_name = "file%d.txt"%nIndex
		file_path = "%s\\%s"%(file_path_name,file_name)
		
		if not os.path.exists(file_path):
			f = open(file_path, 'w')
			if(f):
				f.close()
				
	s = dirlist(file_path_name, [])	
	
def part_test3() :
	class Cat(object) :
		def __init__(self) :
			self.name = name
		def play():
			print ("I Like play")
	
	class BossCat(Cat) :
		def play(ball) :
			print ("I Like play %s" %ball)

	class Person() :	
		def __init__(self,name,age) :
			self.__name = name
			self.__age = age
	
		def get_name(self) :
			return self.__name
		
		def set_name(self,name) :
			self.__name = name	

	class EmailPerson(Person) :
		def __init__(self, name, email) :
			super().__init__(name)
			self.email = email	

	class Student(object) :
		def birth(self) :
			return self._birth
		def birth(self,value) :
			self._birth = value
		def age(self) :
			return 2014-self._birth			

def main():
	part_test1()
	
#Make a script both importable and executable
#让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
if __name__=='__main__':
	main()	