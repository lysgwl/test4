#!/usr/bin/env python
import os
import re
import sys
import cgi

from io import StringIO
from io import BytesIO

from time import ctime
from contextlib import closing

from urllib import request,error
from urllib import parse as urlparse
from threading import Thread, Lock

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(current_path, 'downloads'))

class userThread(Thread):
	def __init__(self, func, args, name=''):
		Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def run(self):
		self.res = self.func(*self.args)

	def result(self):
		return self.res

class userUrl():
	def __init__(self, url):
		self.url = url
		
	def setjoinurl(self, urlscheme, urllocation, urlpath, urlparam):
		url = urlparse.urlunparse((urlscheme, urllocation, urlpath, '', '', ''))
		newurl = urlparse.urljoin(url, urlparam)
			
	def setparseurl(self):
		result = urlparse.urlsplit(self.url)

	def getfilename(self, flag=False):
		if flag == False:
			return os.path.basename(self.url)
		else:
			result = urlparse.urlsplit(self.url)
			len1 = len(result.path) - 1

			while len1 > 0:
				if result.path[len1] == '/':
					break
				len1 = len1 - 1

			filename = result.path[len1+1:len(result.path)]
			if not filename.strip():
				return False
			return filename		

class downloadUrl():
	def __init__(self, url, proxies=None):
		self.url = url
		self.proxies = proxies

	def getfilesize(self):
		try:
			with closing(request.urlopen(self.url, self.proxies)) as req:
				if req.getheader('Content-Length') == None:
					length = 0
				else:	
					length = req.info().get('Content-Length')
		except:
			length = -1
		return int(length)	

	def getfilename(self, openurl=False):
		try:
			filename = userUrl(self.url).getfilename()

			if openurl == True:
				req = request.urlopen(self.url)		#addinfourl对象

				headers = req.getheaders()  		#二元元组列表
				headerinfo = req.info()  			#HTTPMessage对象

				if req.getheader('Content-Disposition') != None:
					if 'Content-Disposition' in headers and headers['Content-Disposition']:
						s = headers['Content-Disposition'].split(';')
				elif req.getheader('Location') != None:
					print("test1")

		except error.URLError as e:
			print(e.reason, ":", e.code)
			print(e.headers)

		return filename		

	def getfiledata(self, *args):
		try:
			#req = request.urlopen(self.url)
			print(self.url)
		except:
			return

class downloadFile():
	def __init__(self, url, blocks=5, proxies=None):
		self.url = url
		self.blocks = blocks
		self.proxies = proxies

	def setdatablocks(self, totalsize):
		ranges = []
		if totalsize < (1024*1024) :
			ranges.append((0, totalsize))
		else:
			blocksize = totalsize / self.blocks	
			for i in range(0, self.blocks-1):
				ranges.append((int(i*blocksize), int(i*blocksize+blocksize-1)))
			ranges.append((int(blocksize*(self.blocks-1)), int(totalsize-1)))
		return ranges

	def downloaddata(self, *args):
		download_url = downloadUrl(self.url)
		download_url.getfiledata(args)

	def downloadfile(self, path):
		download_url = downloadUrl(self.url)
		filesize = download_url.getfilesize()
		if filesize <= 0:
			return
		
		dataBuf = BytesIO()

		ranges = self.setdatablocks(filesize)
		threadname = ["thread_%d" % i for i in range(0, len(ranges))]

		tasks = []
		for i in range(0, len(ranges)):
			task = userThread(self.downloaddata, (dataBuf,ranges[i],), threadname[i])
			task.setDaemon(True)
			task.start()
			tasks.append(task)

		tasks[0].join()		

def main():
	#url = "http://168.130.9.162:8289/login.php"
	url = "https://archive.mozilla.org/pub/seamonkey/releases/2.49.5/win32/en-US/seamonkey-2.49.5.installer.exe"

	download_file = downloadFile(url)
	download_file.downloadfile("")

if __name__ == "__main__":
	main()