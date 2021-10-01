#!/usr/bin/python

try:
	fd = open("C:\\1.Class\\PracticeInClass\\Class26\\exceptionhandling.py","r")
	try:
		fd.write("Hello")
	finally:
		fd.close()
except Exception as e:
	print (e.errno)
	print (e.args)