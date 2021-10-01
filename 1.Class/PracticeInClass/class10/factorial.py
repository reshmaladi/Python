#!C:\Python34

def recursive_factorial(x):
	if (x==1 | x==0 ): return 1
	if x==2 : return 2
	if (x>2):
		return x * recursive_factorial(x-1)
	
def main():
	x= eval(input("enter first number"))
	#y= eval(input("enter second number"))
	print (recursive_factorial(x))

if __name__=="__main__":
	main()