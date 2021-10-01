#!C:\Python34
def isdivisibleby8(no):
	return no & (no-1) 


def main():
	no= eval(input ("enter the number"))
	if (isdivisibleby8(no) == 0):
		print ("Number is divisible by 8")
	else: print ("Number is not divisible by 8")

if __name__=="__main__":
	main()
	

'''
Logic for the program :

Binary representation of 8, 16, 32

8	00001|000
16	00010|000
32	00100|000
64	01000|000
128	10000|000
 
 
 observe that last 3 digits are 000 in all numbers which are divisible by 8 
 so 
 Ex.
	00001000	8
&	
	00000111	7
	===============
	00000000	0
	

	00010000	16
&	
	00001111	15
	===============
	00000000	0	
	
	
'''