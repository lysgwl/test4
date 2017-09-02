#coding=utf-8 
from xlrd import open_workbook

#from collections import OrderedDict  
#from pyexcel_xls import get_data  
#from pyexcel_xls import save_data  

def read_xls_file1():
	x_data1=[]
	y_data1=[]

	wb = open_workbook('1.xlsx')

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
	wb = open_workbook('1.xlsx')
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
		
		for row in range(sheet.nrows):
			for col in range(sheet.ncols):
				print 
		#	rows = sheet.row_values(row)		
		#	print row, ":", rows
		index = index + 1

if __name__ == '__main__': 
	#read_xls_file1()
	read_xls_file2()