#-*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = os.path.abspath(os.path.join(current_path, '2.xls'))

catering_data=file_path

#s1='日期'
#s1.decode('utf-8').encode('gbk')

data = pd.read_excel(catering_data, index_col=u'日期')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()

p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()

y.sort()

for i in range(len(x)):
	if i>0:
		plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
	else:
		plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))
plt.show()