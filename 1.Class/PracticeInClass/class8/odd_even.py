#!C:\Python34
#Write a program to check weather given number is even or add without using arithmetic operator 
def iseven(no):
	if (no & 1==0):
		return True
	return False
	
def isodd(no):
	if(no &1 == 0):
		return False
	return True
	
def main():
	response = iseven(721)
	if response == True:
		print (" Number is even")
	else: print ("number is odd")
	
	
	response = isodd(721)
	if response == False:
		print (" Number is odd")
	else: print ("number is even")
	
	
if __name__=="__main__":
	main()
	

"""
Program logic 
721 	512
209		128
81		64
17		16
1		1

Binary representation of 721 is 
	1011010001
&	
	0000000001
	===========
    0000000000

"""