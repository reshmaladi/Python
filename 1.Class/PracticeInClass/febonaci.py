#!C:\Python34

def febo(num):
	a=1
	b=1
	print (a)
	print (b)
	num= num -2
	while num!=0:
		c= a+b
		print ( c , sep =" ")
		a=b ; b=c
		num= num - 1
def main():
	num  = eval(input ("Enter the number "))
	febo(num)


if __name__=="__main__":
	main()
	
