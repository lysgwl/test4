# -*- coding: UTF-8 -*-
import os
import numpy as np

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = ""

def numpy_test_part1():
	file_path = os.path.abspath(os.path.join(current_path, 'a1.bin'))
	a = np.arange(15).reshape(3,5)	#arange(最小值,最大值,步长)(左闭右开)
	print("array a:%s"%a)
	print("array a:%s"%a.T)									#转置(矩阵)数组: T属性 mT[x][y] = m[y][x]
	print("array a:%s"%(np.dot(a,a.T)))						#计算(矩阵)内积: xTx
	a = np.arange(8).reshape(2,2,2)
	#print("array a: shape=%d, ndim=%d"%(a.shape, a.ndim))	#数组的维度	#数组的行数	
	#print("array a: type=%s, itemsize=%d"%(a.dtype.name, a.itemsize))	#数组的类型名称 #数组中每个元素字节的大小
	#print(type(a))
	#print("array a: size=%d, sum=%d"%(a.size, a.sum()))
	#print("array a: min=%d, max=%d\n"%(a.min(), a.max()))
	
	b = np.ones([10, 10])
	b = np.zeros([10, 10])
	b = np.random.rand(10, 10)		#创建指定形状(示例为10行10列)的数组(范围在0至1之间)
	b = np.empty((10, 10))
	b = np.random.uniform(0, 100)	#创建指定范围内的一个数
	b = np.random.randint(0, 100)	1#创建指定范围内的一个整数
	b = np.random.normal(1.75, 0.1, (4,5))
	b = b[1:3, 2:4]					#截取第1至2行的第2至3列(从第0行算起)
	print("array b:%s\n"%b)
	
	c = np.array([[80,88], [82,81], [84,75], [86,83], [75,81]])
	#c = np.where(c<80, 0, 90)		#如果数值小于80,替换为0;如果大于80,替换为90
	#c = np.amax(c, axis=0)			#求(轴)每一列的最大值,amin
	#c = np.amax(c, axis=1)			#求(轴)每一行的最大值,amin
	#c = np.mean(c, axis=0)			#求(轴)每一列的平均值
	#c = np.mean(c, axis=1)			#求(轴)每一行的平均值
	#c = np.std(c, axis=0)			#求(轴)每一列的方差
	#c = np.std(c, axis=1)			#求(轴)每一行的方差
	#c[:,0] = c[:,0]+5				#为所有成绩都加5分
	print("array c:%s\n"%c)
	
	d = np.array([1,2.6,3], dtype=np.float64)
	d = d.astype(np.int32)
	d = np.array(['1', '2', '3'], dtype=np.string_)
	d = d.astype(np.int32)
	d = d*2
	print("array d:%s"%d)
	
	e = np.random.randint(0,2,size=10000)
	e = (e>0).sum()
	e = np.random.normal(size=(2,2))	#正态分布随机数数组
	print("array e:%s"%e)

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
		
def showinit():
	ret = 0
	value = input("Please input index:").strip()
	if value.isdigit() :
		ret = int(value)
	else :
		ret = -1
		
	return ret	
	
def showmenu(flag):
	ret = 0
	if flag == True :
		print("*****Python Numpy Test*****")
		print("0: show test menu!")
		print("1: numpy test1!")
		print("2: numpy test2!")
		print("3: numpy test3!")
		print("4: numpy test4!")
	
	for index in range (3) :
		ret = showinit()
		if ret < 0 or ret > 4:
			print("Please input: 1 - 4!")
		else :
			break;
			
	return ret
	
def main():
	flag = True;

	while True:
		ret = showmenu(flag)
		if ret == 0 :
			flag = True
			os.system("cls")
		elif ret == 1 :
			flag = False
			numpy_test_part1()
		elif ret == 2 :
			flag = False
			numpy_test_part2()
		elif ret == 3 :	
			flag = False
			numpy_test_part3()
		elif ret == 4 :	
			flag = False
			numpy_test_part4()
			
if __name__=='__main__':
	main()