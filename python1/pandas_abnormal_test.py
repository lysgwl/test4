#-*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

def pandas_test_part1():
	file_path = os.path.abspath(os.path.join(current_path, '2.xls'))

	#s1='日期'
	#s1.decode('utf-8').encode('gbk')

	data = pd.read_excel(file_path, index_col=u'日期')	#读取数据，指定“日期”列为索引列

	plt.rcParams['font.sans-serif'] = ['SimHei']		#用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False			#用来正常显示负号
	plt.figure()										#建立图像

	p = data.boxplot(return_type='dict')				#画箱线图，直接使用DataFrame的方法
	x = p['fliers'][0].get_xdata()						#'flies'即为异常值的标签
	y = p['fliers'][0].get_ydata()

	y.sort()											#从小到大排序，该方法直接改变原对象

	#用annotate添加注释
	#其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
	#以下参数都是经过调试的，需要具体问题具体调试。
	for i in range(len(x)):
		if i>0:
			plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
		else:
			plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))
	plt.show()											#展示箱线图

def pandas_test_part2():
	s = pd.Series([1,2,3], index=['a', 'b', 'c']) #创建一个序列s
	d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns = ['a', 'b', 'c']) #创建一个表
	d2 = pd.DataFrame(s) #也可以用已有的序列来创建表格

	d.head() #预览前5行数据
	d.describe() #数据基本统计量

	#读取文件，注意文件的存储路径不能带有中文，否则读取可能出错。
	pd.read_excel('data.xls') #读取Excel文件，创建DataFrame。
	pd.read_csv('data.csv', encoding = 'utf-8') #读取文本格式的数据，一般用encoding指定编码。

#餐饮销量数据统计量分析	
def pandas_test_part3():
	file_path = os.path.abspath(os.path.join(current_path, '3.xls'))
	
	data = pd.read_excel(file_path, index_col = u'日期') #读取数据，指定“日期”列为索引列
	data = data[(data[u'销量'] > 400)&(data[u'销量'] < 5000)] #过滤异常数据
	statistics = data.describe() #保存基本统计量

	statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
	statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
	statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距
	
	#count:非空值数
	#mean:平均值
	#std:标准差
	#min:最小值
	#
	print(statistics)

#菜品盈利数据 帕累托图	
def pandas_test_part4():
	file_path = os.path.abspath(os.path.join(current_path, '4.xls'))
	
	data = pd.read_excel(file_path, index_col = u'菜品名')
	data = data[u'盈利'].copy()
	#data.sort(ascending = False)

	plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

	plt.figure()
	data.plot(kind='bar')
	plt.ylabel(u'盈利（元）')
	p = 1.0*data.cumsum()/data.sum()
	p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)
	plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，即85%处的标记。这里包括了指定箭头样式。
	plt.ylabel(u'盈利（比例）')
	plt.show()
	
def main():
	#pandas_test_part1()
	#pandas_test_part2()
	#pandas_test_part3()
	pandas_test_part4()
	
if __name__=='__main__':
	main()