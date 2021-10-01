#!C:\Python34

def variabledictionary(a,b,*args, **kwargs):
	print (a,b)
	print (type(args), type(kwargs))
	for x in args:
		print (x)
	for x in kwargs:
		print (x, kwargs[x])
	
def main():
	variabledictionary(10, 20, 1,2,3,5,7,name="test", hobby="testing")
	
if __name__=="__main__":
	main()