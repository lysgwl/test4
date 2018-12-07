# -*- coding: UTF-8 -*-

import os


def StringTest1():
	def test1():
		str1 = 'this is a test!'				#字符串创建和复制
		print(str1[1:2])
		print(str1[5:])
		
		str1 = str1[5:] + '123'					#字符串修改
		print(str1)
		
		#i = 0
		#length = len(str1)
		#while i < length:
		#	print ("char is : %c - %#X" % (str1[i], 108))
		#	i += 1
		
		#str1 = str1[:3] + str1[4:]				#字符串删除
		#print(str1)
		#del str1
		
		#str1 = input("Input your info:")		#输入信息
		#length = len(str1)
		#print(length)
		
		#str1 = isinstance(u'\0xAB', str)		#判断对象的类型
		#print(str1)
		
		#str1 = chr(70)							#用一个范围在range(256)内的整数作参数,返回一个对应的字符
		#str1 = unichr(70)						#返回一个unicode字符
		#str1 = ord('F')						#chr和unichr的配对函数, 以一个字符作为参数, 返回对应的ASCII数值
		#print(str1)
		
	def test2():
		str1 = 'this is a test!'
		str1 = str1.capitalize()				#把字符串第一个字符大写
		#str1 = str1.center(40)					#把字符串居中
		#str1 = str1.count('is')				#返回字符在字符串中出现的次数
		#str1 = str1.endswith('test!')			#检测字符串是否以obj结束
		#str1 = str1.find('is', 4)				#检测字符是否包含在字符串中
		#str1 = str1.isalnum()					#检测字符是否包含数字
		#str1 = str1.isdigit()					#检测字符是否为数字
		#str1 = str1.isalpha()					#检测字符是否为字母
		#str1 = str1.isspace()					#检测字符是否包含空格
		print(str1)
		
	def test3():
		#列表测试1
		list1 = [123, 'abc', 4.56, ['test1', 'test2']]
		print(list1[0])
		print(list1[0:2])
		print(list1[:3])
		
		list1[1] = 'cba'
		print(list1)
		
		del list1[0]
		list1.remove('cba')
		print(list1)
		del list1
		
		#列表测试2
		list1 = ['abc', 123]
		list2 = ['xyz', 789]
		print(list1>list2)
		
		#列表测试3
		
		
	test3()
def main():
	StringTest1()
	
if __name__=='__main__':
	main()