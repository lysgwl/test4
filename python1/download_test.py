#!/usr/bin/env python
import os
import sys

import re
import time
import zipfile
from urllib import request

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(current_path, 'downloads'))

def get_download_file():

	def get_download_file(url, file):
		try:
			req = request.urlopen(url)
			CHUNK = 16*1024
			with open(file, 'wb') as fp:
				while True:
					chunk = req.read(CHUNK)
					if not chunk: break
					fp.write(chunk)
			return True
		except:
			return False
			
	def get_url_version(file):
		try:
			fd = open(file, 'r')
			lines = fd.readlines()
			
			p = re.compile(r'https://www.baidu.com/([0-9]+)\.([0-9]+)\.([0-9]+)')
			
			for line in lines:
				m = p.match(line)
				if m:
					version = m.group(1) + "." + m.group(2) + "." + m.group(3)
					return m.group(0), version
		except:
			raise "get_url_version failed!" % file
		
	download_url = "https://www.blog.pythonlibrary.org/2012/06/07/python-101-how-to-download-a-file/"
	download_file = os.path.join(download_path, "test1")
	
	if not os.path.isdir(download_path):
		os.mkdir(download_path)
		
	if not get_download_file(download_url, download_file):
		raise "download file failed!" % download_url
	
	net_url, net_version = get_url_version(download_file)
	net_unzip_path = os.path.join(download_path, "net-%s" % net_version)
	net_zip_path = os.path.join(download_path, "net-%s.zip" % net_version)
	
	if not get_download_file(net_url, net_zip_path):
		raise "download file failed!" % download_url
		
		
def main():
	get_download_file()
	
if __name__ == "__main__":
	main()