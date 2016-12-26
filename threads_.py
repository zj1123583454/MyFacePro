#!/usr/bin/evn python
#coding:utf-8
try:
	import threading
	from my_module import *
	import time
except:
	print "Error"
	exit()
global flag
flag=False
def a():
	global flag
	flag=True
#threads=[]
#t1=threading.Thread(target=speak,args=(r"./TTS_Voice/开机.wav",))
#t2=threading.Thread(target=a)
#threads=[t1,t2]
if __name__	== "__main__":
	a()
	print flag
	#for t in threads:
		#t.setDaemon(True)
		#t.start()
