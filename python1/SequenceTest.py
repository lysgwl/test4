# -*- coding: UTF-8 -*-

import os


def StringTest1():
	def test1():
		str1 = 'this is a test!'				#�ַ��������͸���
		print(str1[1:2])
		print(str1[5:])
		
		str1 = str1[5:] + '123'					#�ַ����޸�
		print(str1)
		
		#i = 0
		#length = len(str1)
		#while i < length:
		#	print ("char is : %c - %#X" % (str1[i], 108))
		#	i += 1
		
		#str1 = str1[:3] + str1[4:]				#�ַ���ɾ��
		#print(str1)
		#del str1
		
		#str1 = input("Input your info:")		#������Ϣ
		#length = len(str1)
		#print(length)
		
		#str1 = isinstance(u'\0xAB', str)		#�ж϶��������
		#print(str1)
		
		#str1 = chr(70)							#��һ����Χ��range(256)�ڵ�����������,����һ����Ӧ���ַ�
		#str1 = unichr(70)						#����һ��unicode�ַ�
		#str1 = ord('F')						#chr��unichr����Ժ���, ��һ���ַ���Ϊ����, ���ض�Ӧ��ASCII��ֵ
		#print(str1)
		
	def test2():
		str1 = 'this is a test!'
		str1 = str1.capitalize()				#���ַ�����һ���ַ���д
		#str1 = str1.center(40)					#���ַ�������
		#str1 = str1.count('is')				#�����ַ����ַ����г��ֵĴ���
		#str1 = str1.endswith('test!')			#����ַ����Ƿ���obj����
		#str1 = str1.find('is', 4)				#����ַ��Ƿ�������ַ�����
		#str1 = str1.isalnum()					#����ַ��Ƿ��������
		#str1 = str1.isdigit()					#����ַ��Ƿ�Ϊ����
		#str1 = str1.isalpha()					#����ַ��Ƿ�Ϊ��ĸ
		#str1 = str1.isspace()					#����ַ��Ƿ�����ո�
		print(str1)
		
	def test3():
		#�б����1
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
		
		#�б����2
		list1 = ['abc', 123]
		list2 = ['xyz', 789]
		print(list1>list2)
		
		#�б����3
		
		
	test3()
def main():
	StringTest1()
	
if __name__=='__main__':
	main()