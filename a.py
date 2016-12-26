#!/usr/bin/evn python2
#coding:utf-8
import cv2
import time
import cv2.cv as cv
import numpy as np
import shutil
import ctypes
from my_module import *
from facepp import API,File
print '*'*20+"嵌入式实验室人脸识别系统"+'*'*20
flag=False
i=0
API_KEY = '9ffeb1311042de5b6cfec336049b1f16'
API_SECRET = 'k7ukJVKulj9aVjV5v8lJ1uN1pmPzm4IX'

user_api=API(API_KEY,API_SECRET)
openC=ctypes.cdll.LoadLibrary
libso=openC(r"/home/pi/facepp-python-sdk-2.0/rasvoice/demo/samples/tts_sample/libtts_sample.so")
make_voice()
cap=cv2.VideoCapture(0)
success,frame=cap.read()
if success is True:
	print "打开摄像头成功!"
else:
	print "打开摄像头失败!请检查摄像头设备!"
	exit()
speak("./TTS_Voice/开机.wav")
classifier=cv2.CascadeClassifier("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")
cv2.namedWindow("Person")
cv2.namedWindow("Video")
while True:
	while True:
		success,frame=cap.read()
		size=frame.shape[:2]
		image=np.zeros(size,dtype=np.float16)
		image=cv2.cvtColor(frame,cv2.cv.CV_BGR2GRAY)
		cv2.equalizeHist(image,image)
		divisor=8
		h,w=size
		minSize=(w/divisor,h/divisor)
		faceRects=classifier.detectMultiScale(image,1.2,2,cv2.CASCADE_SCALE_IMAGE,minSize)
		cv2.imshow("Video",frame)
		if len(faceRects)>0:
			print '抓取人脸成功!'
			break	
		key=cv2.waitKey(10)
		c = chr(key&255)
		if c in ['q','Q',chr(27)]:
			break
