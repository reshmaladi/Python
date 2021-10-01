#!C:\Python34

def rightmostoff(no, pos , bit):
	x=1
	while(no & x) ==0:
		x =x<<1
		return no & ~ x

def main():
	no = eval(input ("enter the number"))
	pos = eval(input ("enter the pos"))
	bit = eval(input ("enter the bit"))
	print (rightmostoff(no, pos, bit))
	
if __name__=="__main__":
	main()
	
