#!/usr/bin/env python
import os
import re
import sys

from io import StringIO
from io import BytesIO

from time import ctime
from contextlib import closing

from urllib import request
from urllib import parse as urlparse
from threading import Thread, Lock

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(current_path, 'downloads'))

class DownloadThread(Thread) :
	def __init__(self, func, args, name='') :
		Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
		
	def run(self) :
		self.res = self.func(*self.args)
		
	def result(self) :
		return self.res
		
class DownloadFile() :
	def __init__(self, url, proxies=None) :	
		self.url = url
		self.proxies = proxies
		
	def get_filename(self, openurl=False) :
		try :
			if openurl == False :
				return os.path.basename(self.url)
				
			req = request.urlopen(self.url)
			if req.info().has_key('Content-Disposition') :
				filename = req.info()['Content-Disposition'].split('filename=')[1]
				filename = filename.replace('"', '').replace("'", "")
				return filename
			elif req.url != self.url	:
				return os.path.basename(urlparse.urlsplit(req.url)[2])
			else :
				return os.path.basename(self.url)
		except :
			return os.path.basename(self.url)
			
	def get_filesize(self) :
		try :
			with closing (request.urlopen(self.url, self.proxies)) as req :
				length = req.info().get('Content-Length')
			if length is None :
				return 0
			else :
				return int(length)
		except :
			return -1
			
	def get_urldata(self, *args) :
		try :
			res = request.urlopen(self.url)
			print(res.info())
			#print(res.info().headers)
			print(re.read())
			#CHUNK = 16*1024
			#while True:
			#	chunk = req.read(CHUNK)
			#	if not chunk : break
			#	dataBuf.write(chunk)
			#print(self.url)
		except :
			return

class DownloadUrl() :
	def __init__(self, url, path, blocks=5, proxies=None) :
		self.url = url
		self.path = path
		self.blocks = blocks
		self.proxies = proxies
			
	def get_parseurl(self, openurl=None) :
		result = urlparse.urlsplit(self.url)
		urlpath = "%s:\\%s\%s"%(result.scheme, result.netloc, result.path)
		
	def set_datablocks(self, totalsize, blocks) :
		ranges = []
		if totalsize < (1024*1024) :
			ranges.append((0, totalsize))
		else :
			blocksize = totalsize / blocks	
			for i in range(0, blocks - 1):
				ranges.append((int(i*blocksize), int(i*blocksize+blocksize-1)))
			ranges.append((int(blocksize*(blocks-1)), int(totalsize-1)))
		return ranges

	def download_urldata(self) :
		urlfile = DownloadFile(self.url, self.proxies)
		#totalsize = urlfile.get_filesize()
		#if totalsize <= 0 :
		#	return
		
		totalsize = 10
		dataBuf = BytesIO()

		ranges = self.set_datablocks(totalsize, self.blocks)
		threadname = ["thread_%d" % i for i in range(0, len(ranges))]
		
		tasks = []
		for i in range(0, len(ranges)) :
			task = DownloadThread(urlfile.get_urldata, (dataBuf,ranges[i],), threadname[i])
			task.setDaemon(True)
			task.start()
			tasks.append(task)
			
		print(len(tasks))
		tasks[0].join()	
	
def main():
	#download_url = "http://192.168.2.172/sdkMethod/userNumberRuleClass.php"
	download_url = "http://168.130.6.18/login.php"
	#download_url = "https://www.baidu.com"
	#download_url = "https://archive.mozilla.org/pub/seamonkey/releases/2.49.5/win32/en-US/seamonkey-2.49.5.installer.exe"
	
	download = DownloadUrl(download_url, "d:\\")
	download.download_urldata()
	
if __name__ == "__main__":
	main()