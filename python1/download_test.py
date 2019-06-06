#!/usr/bin/env python
import os
import re
import sys

import time
import zipfile

from io import StringIO
from io import BytesIO
from urllib import request

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(current_path, 'downloads'))

def get_urlData_info(url, dataBuf) :
	try:
		req = request.urlopen(url)
		
		CHUNK = 16*1024
		while True:
			chunk = req.read(CHUNK)
			if not chunk : break
			dataBuf.write(chunk)
		return True
		
	except:
		return False
		
def get_userData_info(dataBuf) :
	print("userData!")
		
def get_url_version(dataBuf) :
	try:
		fd = open(dataBuf, 'r')
		lines = fd.readlines()
			
		p = re.compile(r'https://www.baidu.com/([0-9]+)\.([0-9]+)\.([0-9]+)')
			
		for line in lines:
			m = p.match(line)
			if m:
				version = m.group(1) + "." + m.group(2) + "." + m.group(3)
		return m.group(0), version
	except:
			raise "get_url_version failed!" % dataBuf
	
def download_urldata(url) :
	dataBuf = BytesIO()
	if not get_urlData_info(url, dataBuf) :
		return
		
	print("len=%d, data=%s"%(dataBuf.tell(), dataBuf.getvalue()))
	dataBuf.close()
	
def main():
	download_url = "http://192.168.2.172/sdkMethod/userNumberRuleClass.php"
	download_urldata(download_url)
	
if __name__ == "__main__":
	main()