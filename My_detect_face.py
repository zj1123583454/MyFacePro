#!/usr/bin/evn python 
#coding:utf-8
import cv2
import time
import numpy as np
import shutil
import ctypes
from my_module import *
from facepp import API,File
print '*'*20+"嵌入式实验室人脸识别系统"+'*'*20
flag=False
i=0
API_KEY = ''
API_SECRET = ''

user_api=API(API_KEY,API_SECRET)
openC=ctypes.cdll.LoadLibrary
libso=openC(r"./rasvoice/demo/samples/tts_sample/libtts_sample.so")
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
cv2.namedWindow("Video")
while True:
	while True:
		print "读取人脸"
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
	cv2.imwrite('./New_Person/0.jpg',frame)
	shutil.copyfile("./New_Person/0.jpg","./All_Person/"+time.ctime()+".jpg")
	print '等待检测人脸......'
	user_recognition_info=user_api.recognition.recognize(img = File(r'./New_Person/0.jpg'),group_name='test')
	if user_recognition_info['face']==[]:
		flag=False
		print '检测人脸失败!','请调整姿势,以便抓取清晰的人脸!'
	elif user_recognition_info['face'][0]["candidate"][0]["confidence"] <60:
		flag=False
		i=i+1
		if i==3:
			speak("./TTS_Voice/识别.wav")
			speak("TTS_Voice/未识别.wav")
			i=0
		print '数据库中没有此人',i
	else:
		user_recognition_name=user_recognition_info['face'][0]['candidate'][0]["person_name"]
		if user_recognition_name.encode("utf-8")+".wav" not in get_voice():
			libso.tts_begin("你好"+user_recognition_name.encode("utf-8"),r"./TTS_Voice/"+user_recognition_name.encode("utf-8")+".wav")
		speak(r"./TTS_Voice/识别.wav")
		speak(r"./TTS_Voice/"+user_recognition_name.encode("utf-8")+".wav")
		print user_recognition_name
		flag=True
