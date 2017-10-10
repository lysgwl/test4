# -*- coding: UTF-8 -*-
import os
import numpy as np
from scipy import io as spio

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = ""

def scipy_test_part1():
	file_path = os.path.abspath(os.path.join(current_path, 'a1.bin'))
	
def main():
	scipy_test_part1()
	#scipy_test_part2()
	#scipy_test_part3()
	#scipy_test_part4()
	
if __name__=='__main__':
	main()