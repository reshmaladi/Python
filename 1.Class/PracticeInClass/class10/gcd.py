#!C:\Python34

def gcd(x, y):
	
	while (x!=y):
		if x>y :
			x=x-y
		else:
			y=y-x
	return x
	
def recursiongcd(x,y):
	if (x == y): return x
	if (x >y):
		return recursiongcd(x-y, y)  
	return recursiongcd(x, y-x)

def main():
	x= eval(input("enter first number"))
	y= eval(input("enter second number"))
	print (gcd(x, y))
	print (recursiongcd(x, y))

if __name__=="__main__":
	main()
	

