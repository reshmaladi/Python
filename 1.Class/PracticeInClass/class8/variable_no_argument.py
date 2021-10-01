#!C:\Python34

def addargs(*args):
	print (type(args))
	print ( args )
	
	result= 0
	for x in args:
		print (x)
		result = result + x
		print result 
		return result 
	
def main():
	print(addargs(2,3))
	print (addargs(100,200,300,400))
	
if __name__=="__main__":
	main()