#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pyTweetBackUp.py
# Version 1.0
#
# Copyright (C) 2010 - Ershad K <ershad92@gmail.com>
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with <program name>; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, 
# Boston, MA  02110-1301  USA
#

import os, sys, codecs
import time
import twitter

# Change the following values
username = 'USERNAME'
password = 'PASSWORD'
backup_file = 'twitterbackfile' #can also be a path, like /home/user/TweetbackUps
sleep_time = 5 #seconds


fout = codecs.open(backup_file, 'a') #to create such a file
api = twitter.Api(username, password)

while (True):
	time.sleep(sleep_time)
	timeline = api.GetFriendsTimeline(username)
	for s in timeline:
		#print "%s\t%s" % (s.user.name, s.text)
		tweet = s.user.name + "\t" + s.text
		fin = open(backup_file, 'r')
		x = fin.read()
		y = x.find(tweet.encode("utf-8"))
		fin.close()
	
		if y < 0:
			fout = codecs.open(backup_file, 'a')
			text = s.user.name + "\t" + s.text + "\n"
			fout.write(text.encode("utf-8"))
			fout.close()

	



