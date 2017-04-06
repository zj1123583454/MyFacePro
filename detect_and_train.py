#!/usr/bin/evn python
#coding:utf-8
from facepp import API
from facepp import File
import os,sys
from my_module import *
from time import ctime
user_face_id=[]
API_KEY =""
API_SECRET =""
user_api=API(API_KEY,API_SECRET)

user_dir='./Person'
user_new_name=[]
user_all_name = get_person_name(user_dir)
size=len(sys.argv)
if size >1:
	user_argv_name=sys.argv[1:size]
	for i in user_argv_name:
		if i in user_all_name:
			user_new_name.append(i)
		else:
			print "本地没有",i,"这个Person"
			exit()
else:
	user_new_name = get_compare_name('test',user_all_name)
if user_api.info.get_group_list()['group']==[]:
	user.group.create(group_name='test')
if user_new_name!=[]:
	for user_one_name in user_new_name:
		user_all_image = get_person_image(user_dir,user_one_name)
		for user_one_image in user_all_image:
			print user_one_image
			user_detection_info = user_api.detection.detect(img =File(user_one_image))
			if user_detection_info['face'] == []:
				user_error_file = open('./Error_file.txt','aw')
				user_error_file.write(ctime()+'\n'+user_one_image+'\n')
			else:
				#print user_face_info
				user_face_id.append(user_detection_info['face'][0]['face_id'])			
				print user_one_image,user_face_id
		user_person_delete_info=user_api.person.delete(person_name=user_one_name)
		user_person_create_info=user_api.person.create(person_name=user_one_name,group_name='test',face_id=user_face_id)
		user_face_id=[]
		print '成功创建:',user_person_create_info['person_name'],\
			  '人脸数量:',user_person_create_info['added_face'],\
			  '人物ID:',user_person_create_info['person_id']
	
	user_train_info=user_api.recognition.train(group_name='test',type = 'all')
	print user_train_info
	user_api.wait_async(user_train_info['session_id'])
else:
	print '本地没有新加入的person'
	exit()
