#!C:\Python34
print ("Free fall at begining")
def add(a,b):
	return (a+b)
def sub(a,b):
	return (a-b)
def multy(a,b):
	return (a*b)
def divid(a,b):
	return (a//b)
	
def main():
	a= eval(input("Enter first number"))
	b= eval(input("Enter second number"))
	print(add(a,b))
	print( sub(a,b))
	print( multy(a,b))
	print( divid(a,b))
	
if __name__=="__main__":
	main()

print ("Free fall at End")	
	
