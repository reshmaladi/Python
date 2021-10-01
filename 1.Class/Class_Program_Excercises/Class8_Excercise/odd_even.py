#!C:\Python34
# Program to check wheather given number is odd or even without using antithetic operator 

def iseven(no):
	return no & 1


def main():
	no = eval(input ("enter the number"))
	#print (isodd(no))
	if (iseven(no) == 0):
		print ("Even")
	else: print ("Odd")
	
if __name__=="__main__":
	main()