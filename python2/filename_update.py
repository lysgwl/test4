# -*- coding: GBK -*-	#UTF-8

import os
import sys
#import wx
import time
import string
import random
import platform

import Queue
import threading

from ctypes import *

import ConfigParser
from collections import MutableMapping

#import tkinter
#from tkinter import messagebox
#from tkinter import simpledialog

g_config_name = "update.ini"
	
class config_struct:
	def __init__(self):
		self._bInit = False
		self._szFilePath = ''
		self._szFindName = ''
		self._szNewName = ''
		self._bParseName = False
		self._bFindSubDir = False
		self._bOpenSubThread = False
	
	def setconfig(self, bInit, szFilePath, szFindName, szNewName, bParseName, bFindSubDir, bOpenSubThread):
		self._bInit = bInit
		self._szFilePath  = szFilePath
		self._szFindName  = szFindName
		self._szNewName   = szNewName
		self.__bParseName = bParseName
		self._bFindSubDir = bFindSubDir
		self._bOpenSubThread = bOpenSubThread
		
	def getfilepath(self):
		return self._szFilePath
		
	def getfindname(self):
		return self._szFindName
		
	def getnewname(self):
		return self._szNewName
		
	def getparsename(self):
		return self._bParseName
		
	def getfindsubdir_status(self):
		return self._bFindSubDir
		
	def getopensubthread_status(self):
		return self._bOpenSubThread
		
class WorkerThread(threading.Thread):
	def __init__(self, requests_queue, results_queue, poll_timeout=5, **kwds):
		threading.Thread.__init__(self, **kwds)
		self.setDaemon(True)						#
		self._requests_queue = requests_queue		#任务队列
		self._results_queue = results_queue			#任务结果队列
		self._poll_timeout = poll_timeout			#
		self._dismissed = threading.Event()			#线程事件, 如果set线程事件则run会执行break,直接退出工作线程
		self.start()

	def run(self):
		while True:
			if self._dismissed.isSet():									#如果设置了self._dismissed则退出工作线程
				break
			try:
				request = self._requests_queue.get(True, self._poll_timeout)
			except Queue.Empty:												#从任务队列self._requests_queue获取任务，如果队列为空，continue
				continue
			else:
				if self._dismissed.isSet():									#检测此工作线程事件是否被set,如果被设置，意味着要结束此工作线程,那么就需要将取到的任务返回到任务队列中，并且退出线程  
					self._requests_queue.put(request)
					break
				try:														#如果线程事件没有被设置，那么执行任务处理函数request.callable，并将返回的result，压入到任务结果队列中
					result = request.callable(*request.args, **request.kwds)
					self._results_queue.put((request, result))
				except:
					request.exception = True
					self._results_queue.put((request, sys.exc_info()))		#如果任务处理函数出现异常，则将异常压入到队列中 

	def dismiss(self):
		self._dismissed.set()
		
class ThreadPool:
	def __init__(self, num_workers, q_size=0, resq_size=0, poll_timeout=5):	
		self._requests_queue = Queue.Queue(q_size)		#任务队列
		self._results_queue = Queue.Queue(resq_size)	#
		self.workers = []								#工作线程列表
		self.dismissedWorkers = []						#
		self.workRequests = {}							#
		self.createWorkers(num_workers, poll_timeout)
		
	def createWorkers(self, num_workers, poll_timeout=5):
		for i in range(num_workers):
			self.workers.append(WorkerThread(self._requests_queue,
                self._results_queue, poll_timeout=poll_timeout))
			
	def dismissWorkers(self, num_workers, do_join=False):
		dismiss_list = []
		for i in range(min(num_workers, len(self.workers))):
			worker = self.workers.pop()
			worker.dismiss()
			dismiss_list.append(worker)
			
		if do_join:
			for worker in dismiss_list:
				print("1")
                #worker.join()
		else:
			self.dismissedWorkers.extend(dismiss_list)

	def joinAllDismissedWorkers(self):
		for worker in self.dismissedWorkers:
			worker.join()
        #self.dismissedWorkers = []
		
	def putRequest(self, request, block=True, timeout=None):
		assert isinstance(request, WorkRequest)
		
		self._requests_queue.put(request, block, timeout)
		self.workRequests[request.requestID] = request
		
	def poll(self, block=False):
		while True:
			if not self.workRequests:
				return
			elif block and not self.workers:
				return
				
			try:
				request, result = self._requests_queue.get(block=block)
			except Queue.Empty:
				break
	def wait(self):
		while 1:
			print('2')
			
class WorkRequest:
	def __init__(self, callable_, args=None, kwds=None, requestID=None, callback=None): #exc_callback=_handle_thread_exception
		if requestID is None:
			self.requestID = id(self)
		else:
			try:
				self.requestID = hash(requestID)
			except TypeError:
				raise TypeError("requestID must be hashable.")
				
		self.exception = False
		self.callback = callback
#		self.exc_callback = exc_callback
		self.callable = callable_
		self.args = args or []
		self.kwds = kwds or {}
		
	def __str__(self):
		print("1")
		return "<WorkRequest id=%s args=%r kwargs=%r exception=%s>" % \
            (self.requestID, self.args, self.kwds, self.exception)			
			
def makeRequests(callable_, args_list, callback=None):
	requests = []
	for item in args_list:
		print(item)
		if isinstance(item, tuple):
			requests.append(WorkRequest(callable_, item[0], item[1], callback=callback))
		else:
			requests.append(WorkRequest(callable_, [item], None, None))
	return requests		
			
def check_system_type():
	return platform.system()		
		
def print_warning_wnd(wndInfo, wndTitle, flags):
	ret = 0
	sysstr = check_system_type()
	
	if (sysstr == "Windows"):
		user32 = windll.LoadLibrary('user32.dll')
		ret = user32.MessageBoxA(0, wndInfo.encode('gbk'), wndTitle.encode('gbk'), flags)	#str.encode(wndInfo)	str.encode(wndTitle)
		if (ret == 6):
			return 1
		elif (ret == 7):
			return 0
		else:
			return 0
	elif (sysstr == "Linux"):
		print("Call Linux tasks")
	else:
		print("Other System tasks")
		
def check_config_file(filepath):
	return os.path.exists(filepath)
	
def init_config_file(filepath):
	try:
		f = open(filepath, 'w')
		
		config = ConfigParser.ConfigParser()
		config.add_section('config')
		config.set("config", "FilePath", "")
		config.set("config", "FindName", "")
		config.set("config", "NewName", "")
		config.set("config", "bParseName", "0")
		config.set("config", "bFindSubDir", "0")
		config.set("config", "bOpenSubThread", "0")		
		config.write(f);
	finally:
		if f:
			f.close()

def read_config_file(filepath):
	bParseName = False
	bFindSubDir = False
	bOpenSubThread = False
	
	configInfo = config_struct()
	config = ConfigParser.ConfigParser()
	config.read(filepath)
	
	findPath = config.get("config", "FilePath")
	findName = config.get("config", "FindName")
	newName  = config.get("config", "NewName")
	
	isParseName  = config.get("config", "bParseName")
	isFindSubDir = config.get("config", "bFindSubDir") 
	isOpenSubThread = config.get("config", "bOpenSubThread");
	
	if (isParseName == "" or isParseName == "0" or isParseName == "False" or isParseName == "FALSE") :
		bParseName = False
	elif (isParseName == "1" or isParseName == "True" or isParseName == "TRUE"):
		bParseName = True
	else:
		bParseName = False
		
	if (isFindSubDir == "" or isFindSubDir == "0" or isFindSubDir == "False" or isFindSubDir == "FALSE"):
		bFindSubDir = False
	elif (isFindSubDir == "1" or isFindSubDir == "True" or isFindSubDir == "TRUE"):
		bFindSubDir = True
	else:
		bFindSubDir = False
	
	if (isOpenSubThread == "" or isOpenSubThread == "0" or isOpenSubThread == "False" or isOpenSubThread == "FALSE"):
		bOpenSubThread = False
	elif (isOpenSubThread == "1" or isOpenSubThread == "True" or isOpenSubThread == "TRUE"):
		bOpenSubThread = True
	else:
		bOpenSubThread = False
		
	configInfo.setconfig(True, findPath, findName, newName, bParseName, bFindSubDir, bOpenSubThread)
	return configInfo

def enum_files(filepath):
	for name in os.listdir(dirpath):
		full_path = os.path.join(dirpath, name)
		if os.path.isdir(full_path):
			for entry in enumfile(full_path):
				yield entry
		elif os.path.isfile(full_path):
			yield full_path
		else:
			print("It could be a symbolic link! %s" % full_path)

def test1(s1, s2, wq):
	try:
		print(s1)
		print(s2)
	except os.error as msg:
		return
		
def test2(data):
	result = round(random.random()*data, 5)
	return result
	
def test3(request, result):
	print("Result %s:%r" % (request.requestID, result))
	
def enum_threadproc(configInfo):
	print(configInfo.getfilepath())
	
def	main():
#	reload(sys)
#	sys.setdefaultencoding('utf-8')

	abs_path_name = os.path.dirname(__file__)
	cur_path_name = os.path.abspath(abs_path_name)
	configfile_path_name = cur_path_name + "\\" + g_config_name
	
	strWndInfo = u'没有找到配置文件,是否初始化配置文件?'

	if not check_config_file(configfile_path_name):
		ret = print_warning_wnd(strWndInfo, u"警告!", 4)
		if(ret == 1):
			if not init_config_file(configfile_path_name):
				return 
		else:
			return	
		
	#messagebox.askquestion('Python Tkinter', 'askokcancel')		
	configInfo = read_config_file(configfile_path_name)

	if(configInfo.getfilepath() == ""):
		print_warning_wnd(u"查找路径信息不能为空, 请检查！", u"警告!", 1)
		return
	else:	
		#t = threading.Thread(target=enum_threadproc, args=(configInfo,))
		#threads.append(t)
		#t.start()
		#t.join()
		
		data1 = [random.randint(1,10) for i in range(20)]
		print(data1)
		
		requests = makeRequests(test2, data1, test3)
		
		data2 = [((random.randint(1,10),), {}) for i in range(20)]
		print(data2)
		
		requests.extend(makeRequests(test2, data2, test3))
		
		task = ThreadPool(1)
		task.putRequest(requests[0])
		

if __name__=='__main__':
	main()	