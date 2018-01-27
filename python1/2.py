#!/usr/bin/env python
import os
import sys

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)

python_path = os.path.abspath(os.path.join(current_path, os.pardir, 'python27', '1.0'))
noarch_lib = os.path.abspath(os.path.join(python_path, 'lib', 'noarch'))

root_path = os.path.abspath(os.path.join(current_path, os.pardir))
download_path = os.path.abspath(os.path.join(root_path,os.pardir, os.pardir, 'data', 'downloads'))

import urllib2
import time
from instances import xlog
import zipfile
import config

opener = urllib2.build_opener()

def get_net():
	global net_unzip_path
	def download_file(url, file):
		try:
			xlog.info("download %s to %s", url, file)				req = opener.open(url)
			CHUNK = 16 * 1024
			with open(file, 'wb') as fp:
				while True:
					chunk = req.read(CHUNK)
					if not chunk: break
					fp.write(chunk)
			return True				
		except:	
			xlong.info("download %s to %s fil", url, file)
			return False
	def get_net_url_version(readme_file):
			
def update_env():
	get_net()

#https://www.cnblogs.com/jackyspy/p/6027385.html
def wait_net_exit():
	
	def http_request(url, method="GET"):
		proxy_handler = urllib2.ProxyHandler({})
		opener = urllib2.build_opener(proxy_handler)
		try:
			req = opener.open(url)
			return req
		except Exception as e:
			return False
	for i in range(20):
		host_port = config.get(["modbules", "launcher", "control_port"], 8085)
		req_url = "http://127.0.0.1:{port}/quit".format(port=host_port)	
		if http_request(req_url) == False:
			return True
		time.sleep(1)
	return False

def main():
	wait_net_exit()
	update_env()

if __name__ == "__main__":
	main()
	
