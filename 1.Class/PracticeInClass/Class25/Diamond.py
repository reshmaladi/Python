#!/usr/bin/python

import inspect

class A(object):
	def methodM(self):
		print ("Inside Class A: Method M")
	def methodK(self):
		print ("Inside Class A: Method K")
class B(A):
	def methodL(self):
		print ("Inside Class B: Method L")
		
class C(A):
	def methodN(self):
		print ("Inside Class C : Method N")
	def methodM(self):
		print ("Inside Class C: Method M")

class D(B,C):
	def methodR(self):
		print("Inside Class D")

def main():
	d =D()
	d.methodR()
	d.methodM()
	d.methodK()
	print (inspect.getmro(D))

if __name__=="__main__":
	main()