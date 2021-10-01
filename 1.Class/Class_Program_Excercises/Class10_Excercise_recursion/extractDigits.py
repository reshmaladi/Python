#!C:\Python34

def extract_digit(x):
	if x=="":
		return 0
	elif type(
		return extract_digit(x[1:])


def main():
	x= str(input("enter first number"))
	#y= eval(input("enter second number"))
	print (recursive_length(x))

if __name__=="__main__":
	main()
	