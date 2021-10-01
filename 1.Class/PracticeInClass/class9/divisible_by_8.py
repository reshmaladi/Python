#!C:\Python34

def divisibleby8(no):
	return (no & 7) == 0
	
def main():
	no= eval(input ("enter the number"))
	
	print (divisibleby8(no))

if __name__=="__main__":
	main()
	