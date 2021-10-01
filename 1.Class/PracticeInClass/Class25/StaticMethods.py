#!/usr/bin/python

class demo:
	@staticmethod
	def InvokeStatic():
		print("Static method")
	@classmethod
	def InvokeClassMethod(cls):
		print("Inside class method",type(cls),id(cls))
	def InvokeObjectMethods(self):
		print ("Inside object method")
		
demo.InvokeStatic()
demo.InvokeClassMethod()
print(id(demo))
d =demo()
d.InvokeObjectMethods()

'''
One more 
d =demo()
d.InvokeStatic()
'''