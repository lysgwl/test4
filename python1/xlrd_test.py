#coding=utf-8 

import os
from xlrd import open_workbook
#from __future__ import print_function

#from collections import OrderedDict  
#from pyexcel_xls import get_data  
#from pyexcel_xls import save_data  

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = os.path.abspath(os.path.join(current_path, '1.xlsx'))

def read_xls_file1():
	x_data1=[]
	y_data1=[]

	wb = open_workbook(file_path)

	for s in wb.sheets():
		print 'Sheet:',s.name
		for row in range(s.nrows):
			print 'the row is:',row
			values = []
			for col in range(s.ncols):
				values.append(s.cell(row,col).value)
			print values
			x_data1.append(values[0])
			y_data1.append(values[1])

def read_xls_file2():
	wb = open_workbook(file_path)
	print wb.sheet_names()
	
	index = 0
	for s in wb.sheets():
		print index, "-", s.name
		
		sheet = wb.sheet_by_index(index)	#sheet = sheet_by_name('Sheet1')
		print sheet.name, sheet.nrows, sheet.ncols
		
		#print sheet.cell(0,0).value.encode('gbk')
		#print sheet.cell_value(0,0).encode('gbk')
		#print sheet.row(0)[0].value.encode('gbk')
		#print sheet.cell(0,0).ctype
		
		pre_row = 0
		for row in range(sheet.nrows):
			for col in range(sheet.ncols):
				type = sheet.cell_type(row,col)
				value = sheet.cell(row,col).value;

				if row != pre_row:
					print
				pre_row = row
				#print "321", "#", row, pre_row,type,value,
				
				if type == 0 or value == '':
					if col == (sheet.ncols - 1):
						print
					continue
					
				if type == 1:
					value = value.encode('gbk')
				
				if col == (sheet.ncols - 1):
					print('%d-%d'%(row,col)), ":", value
				else:
					print('%d-%d'%(row,col)), ":", value,
		index = index + 1

if __name__ == '__main__': 
	read_xls_file1()
	#read_xls_file2()