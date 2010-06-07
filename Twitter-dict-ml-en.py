#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pyTweetBackUp.py
# Version 1.0
#
# Copyright (C) 2010 - Ershad K <ershad92@gmail.com>
#
# Licensed under GPL Version 3

import os, sys, codecs
import time
import twitter
from dictdlib import DictDB

# Change the following values
username = 'USERNAME'
password = 'PASSWORD'
backup_file = 'twitterbackfile' #File name of Path + File name
sleep_time = 1 #seconds

api = twitter.Api(username, password)

while (True):
	y = -1
	time.sleep(sleep_time)
	timeline = api.GetReplies()
	for s in timeline:
		#print "%s --> %s" % (s.user.name, s.text)

		tweet = s.user.name + "\t" + s.text
		y = tweet.find("dict")

		if y > 0:
			fin = open(dataFile, 'r')
			x = fin.read()
			y = x.find(s.id.encode("utf-8",'ignore'))
			fin.close()
	
		if y < 0:
			print "%s --> %s" % (s.user.name, s.text)
			word = s.text[13:]
			print word			
			en_ml_db = DictDB("freedict-eng-mal")
			try:
				definition = en_ml_db.getdef(word)[0]
			except:	
				definition =  "No definitions found"
			print definition
			defi = definition [0:110]
		
			output = '@' + s.user.screen_name + ' ' + defi
			print output
			api.PostUpdate (output.decode("utf-8",'ignore'))



