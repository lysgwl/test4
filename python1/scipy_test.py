# -*- coding: UTF-8 -*-
import os
import numpy as np
from scipy import io as spio
from scipy.optimize import fsolve #������ⷽ����ĺ���
from scipy import integrate #������ֺ���

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = ""

def f(x): #����Ҫ���ķ�����
  x1 = x[0]
  x2 = x[1]
  return [2*x1 - x2**2 - 1, x1**2 - x2 -2]
  
def g(x): #���屻������
  return (1-x**2)**0.5  
  
def scipy_test_part1():
	file_path = os.path.abspath(os.path.join(current_path, 'a1.bin'))
	
def scipy_test_part2():
	result = fsove(f, [1,1]) #�����ֵ[1, 1]�����
	print(result) #��������Ϊarray([ 1.91963957,  1.68501606])
	
def scipy_test_part3():
	pi_2, err = integrate.quad(g, -1, 1) #���ֽ�������
	print(pi_2 * 2) #��΢����֪ʶ֪�����ֽ��ΪԲ����pi��һ��
	
def main():
	#scipy_test_part1()
	#scipy_test_part2()
	#scipy_test_part3()
	#scipy_test_part4()
	
if __name__=='__main__':
	main()