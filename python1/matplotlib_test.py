# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def matplotlib_test_part1():
	x = np.linspace(0, 10, 500)
	dashes = [10, 5, 100, 5]

	fig, ax = plt.subplots()
	line1, = ax.plot(x, np.sin(x), '--', linewidth=2, label='Dashes set retroactively')
	line1.set_dashes(dashes)

	line2, = ax.plot(x, -1*np.sin(x), dashes=[30,5, 10, 5], label='Dashes set proactively')

	ax.legend(loc='lower right')
	plt.show()
	
def matplotlib_test_part2():
	x = np.linspace(0, 10, 1000) #作图的变量自变量
	y = np.sin(x) + 1 #因变量y
	z = np.cos(x**2) + 1 #因变量z

	plt.figure(figsize = (8, 4)) #设置图像大小
	plt.plot(x,y,label = '$\sin x+1$', color = 'red', linewidth = 2) #作图，设置标签、线条颜色、线条大小
	plt.plot(x, z, 'b--', label = '$\cos x^2+1$')  #作图，设置标签、线条类型
	plt.xlabel('Time(s) ') # x轴名称
	plt.ylabel('Volt') # y轴名称
	plt.title('A Simple Example') #标题
	plt.ylim(0, 2.2) #显示的y轴范围
	plt.legend() #显示图例
	plt.show() #显示作图结果

def main():
	#matplotlib_test_part1()
	#matplotlib_test_part2()
	#matplotlib_test_part3()
	#matplotlib_test_part4()
	
if __name__=='__main__':
	main()