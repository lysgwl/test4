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
	x = np.linspace(0, 10, 1000) #��ͼ�ı����Ա���
	y = np.sin(x) + 1 #�����y
	z = np.cos(x**2) + 1 #�����z

	plt.figure(figsize = (8, 4)) #����ͼ���С
	plt.plot(x,y,label = '$\sin x+1$', color = 'red', linewidth = 2) #��ͼ�����ñ�ǩ��������ɫ��������С
	plt.plot(x, z, 'b--', label = '$\cos x^2+1$')  #��ͼ�����ñ�ǩ����������
	plt.xlabel('Time(s) ') # x������
	plt.ylabel('Volt') # y������
	plt.title('A Simple Example') #����
	plt.ylim(0, 2.2) #��ʾ��y�᷶Χ
	plt.legend() #��ʾͼ��
	plt.show() #��ʾ��ͼ���

def main():
	#matplotlib_test_part1()
	#matplotlib_test_part2()
	#matplotlib_test_part3()
	#matplotlib_test_part4()
	
if __name__=='__main__':
	main()