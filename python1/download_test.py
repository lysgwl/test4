#!/usr/bin/env python
import os
import re
import sys

import time
import zipfile

from io import StringIO
from io import BytesIO
from urllib import request
from urllib import parse as urlparse

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(current_path, 'downloads'))

def get_filename(url, openurl=False) :
	try :
		if openurl == False :
			return os.path.basename(url)
		
		req = request.urlopen(url)
		if req.info().has_key('Content-Disposition') :
			filename = req.info()['Content-Disposition'].split('filename=')[1]
			filename = filename.replace('"', '').replace("'", "")
			return filename
		elif req.url != url	:
			return os.path.basename(urlparse.urlsplit(req.url)[2])
		else :
			return os.path.basename(url)
	except :
		return os.path.basename(url)
		
def get_parseurl(url, openurl=None) :
	result = urlparse.urlsplit(url)
	urlpath = "%s:\\%s\%s"%(result.scheme, result.netloc, result.path)
		
def get_urlfilesize(url) :
	try :
		req = request.urlopen(url)
		headers = req.info().headers
		
		length = 0
		for header in headers :
			if header.find('Length') != -1 :
				length = header.split(':')[-1].strip
				length = int(length)
		return length
	except :
		return -1
	
def get_urldata(url, dataBuf) :
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
				
def download_urldata(url) :
	dataBuf = BytesIO()
	print(get_urlfilesize(url))
	
def main():
	#download_url = "http://192.168.2.172/sdkMethod/userNumberRuleClass.php"
	download_url = "http://168.130.6.18/login.php"
	download_urldata(download_url)
	
if __name__ == "__main__":
	main()