# -*- coding: UTF-8 -*-

import os
import sys

from io import BytesIO

def test1(*args) :
	for i in args :
		print(i)

def test2(**kwargs) :
	for i in kwargs :
		print(kwargs[i])

def test3(*args) :
	for i in args :
		i.write("3333".encode('utf-8'))
		print(i.getvalue())

def test4(args) :
	print(args)
	#args.write("3333".encode('utf-8'))
	#print(args.getvalue())
	args[0].write("3333".encode('utf-8'))
	print(args[1])

def test5(func, args) :
	func(*args)

def test(*args) :
	print(args)
	args[0].write("4444".encode('utf-8'))

def main() :
	#test1(1, 2, 3)
	#test2("1", 2, "3")

	dataBuf = BytesIO()
	#test3(dataBuf)
	#test4((dataBuf,1,))

	test5(test, (dataBuf, 1,))
	print("wl-%s"%(dataBuf.getvalue()))

if __name__ == "__main__" :
	main()