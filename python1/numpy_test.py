# -*- coding: UTF-8 -*-
import os
import numpy as np

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = ""

def numpy_test_part1():
	file_path = os.path.abspath(os.path.join(current_path, 'a1.bin'))
	
	#tofile
	a = np.arange(0,12)
	a.shape = 3,4
	a.tofile(file_path)
	print(a.dtype)
	
	#fromfile
	if a.dtype == 'float':
		dtype = np.float
	elif a.dtype == 'int32':
		dtype = np.int32
	else:
		return
		
	b = np.fromfile(file_path, dtype=dtype)
	print(b)
	b.shape = 3,4
	print(b)
	#print(b["arr_0"])

def numpy_test_part2():
	file_path = os.path.abspath(os.path.join(current_path, 'a2.npz'))
	
	#
	a = np.array([[1,2,3],[4,5,6]])
	b = np.arange(0, 1.0, 0.1)
	c = np.sin(b)
	
	np.savez(file_path, a, b, sin_array=c)
	
	#
	r = np.load(file_path)
	print(r["arr_0"])
	print(r["arr_1"])
	print(r["sin_array"])

def numpy_test_part3():
	file_path1 = os.path.abspath(os.path.join(current_path, 'a3_1.txt'))
	
	#
	a = np.arange(0, 12, 0.5)
	a.reshape(4,-1)
	
	np.savetxt(file_path1, a)
	
	#
	b = np.loadtxt(file_path1)
	print(b)
	
	file_path2 = os.path.abspath(os.path.join(current_path, 'a3_2.txt'))
	#保存为证书，以逗号分隔
	c = np.savetxt(file_path2, a, fmt="%d", delimiter=",")
	
	#
	d = np.loadtxt(file_path2, delimiter=",")
	print(d)
	
def numpy_test_part4():
	file_path1 = os.path.abspath(os.path.join(current_path, 'a4_1.npz'))
	
	#
	a = np.arange(8)
	print(a)
	b = np.add.accumulate(a)
	print(b)
	c = a + b
	print(c)
	
	#
	f = file(file_path1, "wb")
	np.save(f, a)
	np.save(f, b)
	np.save(f, c)
	f.close()
	
	#
	f = file(file_path1, "rb")
	a = np.load(f)
	print(a)
	b = np.load(f)
	print(b)
	c = np.load(f)
	print(c)

def numpy_test_part5():
	a = np.array([2, 0, 1, 5]) #创建数组
	print(a) #输出数组
	print(a[:3]) #引用前三个数字（切片）
	print(a.min()) #输出a的最小值
	a.sort() #将a的元素从小到大排序，此操作直接修改a，因此这时候a为[0, 1, 2, 5]
	b= np.array([[1, 2, 3], [4, 5, 6]]) #创建二维数组
	print(b*b) #输出数组的平方阵，即[[1, 4, 9], [16, 25, 36]]
	
def main():
	#numpy_test_part1()
	#numpy_test_part2()
	#numpy_test_part3()
	#numpy_test_part4()
	#numpy_test_part5()
	
if __name__=='__main__':
	main()