#!C:\Python34
def add(a, b, c=0, d=0, e=0):
	return a+b+c+d+e
	
	
def multi(a, b, c=1, d=1, e=1):
	return a*b*c*d*e
	
def main():
	print (add(2,3))
	print (add(2,3,4))
	print (add(2,3,4,5))
	print (add(2,3,4,5,6))

	print (multi(2,3))
	print (multi(2,3,4))
	print (multi(2,3,4,5))
	print (multi(2,3,4,5,6))
if __name__=="__main__":
	main()