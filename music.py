#!/usr/bin/env python2
#coding:utf-8
import pygame,time
import sys
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("./TTS_Voice/"+sys.argv[1])
channela = sounda.play()
while channela.get_busy():
	pygame.time.delay(300)
