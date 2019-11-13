# -*- coding: UTF-8 -*-

import os
import sys

from time import ctime
from urllib import request
from threading import Thread, Lock

class CTest(Thread) :
	def __init__(self, func, args, name='') :
		Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
		
	def run(self) :
		print("Test1:", ctime())
		self.res = self.func(*self.args)
		print("Test2:", ctime())
	
	def getresult(self) :
		return self.res
		
def thread_run1(x) :
	print("thread_run1 = %d"%(x+1))
	return x+1
	
def main() :
	url = "http://168.130.6.18/login.php"
	
	threads = []
	for i in range(3) :
		t = CTest(thread_run1, (i,), thread_run1.__name__)
		threads.append(t)
		
	for i in range(3) :
		threads[i].start()
		
	for i in range(3) :
		threads[i].join()
		print(threads[i].getresult())
		
if __name__ == "__main__" :
	main()	