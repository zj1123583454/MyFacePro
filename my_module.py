#!/usr/bin/evn python 
#coding:utf-8
from facepp import API
from facepp import File
import os
API_KEY = ''
API_SECRET = ''
user_api=API(API_KEY,API_SECRET)

def get_person_name(user_dir):
	user_all_PersonName=[]
	if os.path.exists(user_dir):
		user_all_name=os.listdir(user_dir)
		for x in user_all_name:
			b=os.path.join(user_dir,x)
			if os.path.isdir(b):
				user_all_PersonName.append(x)
	else:
		return False
	return user_all_PersonName

def get_person_image(user_dir,user_name):
	if type(user_name) !=list:
		user_name=[user_name]
	user_text=['.jpg','jpeg','png']
	user_all_image=[]
	print user_name
	for i in user_name:
		user_person_dir=os.path.join(user_dir,i)
		user_filename=os.listdir(user_person_dir)
		for j in user_filename:
			k=os.path.join(user_person_dir,j)
			if os.path.isfile(k):
				if os.path.splitext(k)[1] in user_text:
					user_all_image.append(k)
	return user_all_image

def get_compare_name(group_name='test',name=[]):
	user_allname=[]
	compare_name=[]
	allname=user_api.group.get_info(group_name=group_name)
	for b in allname['person']:
		user_allname.append(b[u'person_name'.encode('utf-8')])
	for x in name:
		if x.decode('utf-8') not in user_allname:
			compare_name.append(x)
	return compare_name

def speak(filename):
	import pygame,time
	pygame.init()
	pygame.mixer.init()
	sounda= pygame.mixer.Sound(filename)
	channela = sounda.play()
	while channela.get_busy():
		pygame.time.delay(100)

def get_voice():
	import os
	user_all_voice=[]
	user_join_dir="./TTS_Voice"
	user_voice=os.listdir(user_join_dir)
	for j in user_voice:
		k=os.path.join(user_join_dir,j)
		if os.path.isfile(k):
 			if os.path.splitext(k)[1]== ".wav":
				os.path.split(k)
				user_all_voice.append(os.path.split(k)[1])
	return user_all_voice
def make_voice():
	import ctypes
	openC=ctypes.cdll.LoadLibrary
	libso=openC(r"./rasvoice/demo/samples/tts_sample/libtts_sample.so")
	name={"识别.wav":"识别结果","未识别.wav":"数据库中没有此人","开机.wav":"嵌入式实验室人脸识别系统启动成功"}
	for i,j in name.iteritems():
		if i not in get_voice():
			print i,j
			libso.tts_begin(j,r"./TTS_Voice/"+i)
			print '语音文件加载成功'
