#!/usr/bin/python

# 
# Copyright (c) 2015, Shilin Victor <chrono.monochrome@gmail.com>
# 
# This software is licensed under the terms of the GNU General Public
# License version 2, as published by the Free Software Foundation, and
# may be copied, distributed, and modified under those terms.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# General Public License for more details.
#
# 

import sys, os
from ftplib import FTP

def usage():
	print("usage: ./uploader.py password local_file_name remote_dir_name")
	exit()

if (len(sys.argv) < 4):
	usage()
	exit()

DEBUG = 1
VERBOSE_DEBUG = 0	

SERVER = "ftp.strato.de"
USER = "xda@xda.mister-freeze.eu"
PASSWORD = sys.argv[1]
TIMEOUT = 99999999
LOCAL_FILE=sys.argv[2]
REMOTE_DIR="./%s" % sys.argv[3]

def debug_print(s, verbose_debug_flag = 1, traceback = 0):
	if DEBUG and verbose_debug_flag:
		os.system("echo %s"%s)

def upload():
	try:
		con = FTP(SERVER, USER, PASSWORD, USER, TIMEOUT)
	except:
		debug_print("cant connect to %s@%s" % (SERVER, USER))
		os.system("echo error: %s" % str(sys.exc_info()[1]))
		exit()

	debug_print("connected to %s@%s" % (SERVER, USER))
	
	try:
		con.cwd(REMOTE_DIR)
	except:
		debug_print("cant change folder to %s" % (REMOTE_DIR))
		os.system("echo error: %s" % str(sys.exc_info()[1]))
		exit()

	debug_print("changed folder to to %s" % (REMOTE_DIR))


	remote_name = LOCAL_FILE.split("/")[-1]

	try:
		con.storbinary("STOR %s" % (remote_name), open(LOCAL_FILE,"rb"))
	except:
		debug_print("upload failed")
		os.system("echo error: %s" % str(sys.exc_info()[1]))
		exit()

	debug_print("successfully uploaded")

upload()
