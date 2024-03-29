"""
	Summary lecture11 
	10/2/19
"""
#swapping bits 
#	x=1512	10111101000
#	y=1234	10011010010
#	pos=7 , bits=4
#here we need binary with 4 1's at pos = 00001111000
"""
def SwapBits(x,y,pos,bits):
	mask=( 1 << bits ) - 1  # here we get bin num with 4 1's  = 00000001111
	mask=mask<<(pos - bits) # mask at pos = 00001111000
	x_part=x & mask		#here we get 4 bits from 7  x_part=00001101000
	y_part=y & mask		#similarly					y_part=00001010000
	x=x & ~mask			#here we replace 4 bits to zero in x  x=10110000000
	y=y & ~mask			#similarly							  y=10010000010
	x=x | y_part		#or operation will replace 4 bits from 0 to y_part bits only remaining will be same 	x=10111010000
	y=y | x_part		#similarly 																				y=10011101010
	return x,y
	
def main():
	x,y,pos,bits=eval(input("enter x,y,position,bits : "))
	print(SwapBits(x,y,pos,bits)" ")
	
if __name__ == '__main__' :
	main()
"""
# swap different positions of both numbers
""" 
def SwapDiffBits(x,y,x_pos,y_pos,bits):
	mask=( 1 << bits ) - 1 
	x_mask=mask<<(x_pos - bits)
	y_mask=mask<<(y_pos - bits)
	x_part=x & mask		
	y_part=y & mask		
	if x_pos > y_pos :					
		x_part=x_part >>(x_pos-y_pos)		#shift x part to y position bits by right shift
		y_part=y_part <<(x_pos-y_pos)		#shift y part to x position bits by left shift  
	else:										#similarly for if y pos greater
		x_part=x_part <<(y_pos-x_pos)
		y_part=y_part >>(y_pos-x_pos)
	x=x & ~x_mask			
	y=y & ~y_mask
	x=x | y_part		
	y=y | x_part		
	return x,y
	
def main():
	x,y,x_pos,y_pos,bits=eval(input("enter x,y,x_position,y_position,bits : "))
	print(SwapDiffBits(x,y,x_pos,y_pos,bits))
	
if __name__ == '__main__' :
	main()
"""

#HW
#move all bitwise programs in a single file and write a menu driven program.

#HW
#move all patterns programs in a single file and write a menu driven program.

#HW
#wap to add 2 nums w/o using arithmetic operator
#	Hint: use  | ,& ,<<, >> 
#			e.g to add use | 
#			if same num then do andding , shift num by 1 


# wap to accept 2 numbers from usr and find its gcd
"""
def RecursiveGCD(num1,num2):
	if num1 == num2 :
		return num1
	if num1 > num2 :
		return RecursiveGCD(num1-num2,num2)       
	return RecursiveGCD(num1,num2-num1)

def GCD(num1,num2):
	while num1 != num2 :
		if num1 > num2:
			num1=num1-num2
		else:
			num2=num2-num1
	return num1
def main():
	num1,num2=eval(input("Enter 2 number to find gcd : "))
	print("gcd of "+str(num1)+" and "+str(num2)+" is : "+str(GCD(num1,num2)))
	print("gcd of "+str(num1)+" and "+str(num2)+" is : "+str(RecursiveGCD(num1,num2)))	
	
if __name__ == "__main__" :
	main()
"""
#dry RUN for gcd:
"""
GDC(21,35) | RecursiveGCD(21,35)
	21,35
		21,14
			7,14
				7,7
					return 7
"""

#BOOK to read : programming language pragmatics - Michael Scott

#HW
# Draw stack frame for 128,96 i.e function call stack from main to main with function calls with values and return with value

"""
Recursion
Direct InDirect
A->A	A->B->A
"""

#write a Recursive program to find factorial of number
"""
def R_Factorial(num):
	if num == 0 or num == 1:
		return 1
	if num == 2 :
		return 2
	return num * R_Factorial(num-1)
	
def main():
	num=int(input("Enter to number to find factorial: "))
	print("Factorial of number"+str(num)+" is : "+str(R_Factorial(num)))

if __name__ == '__main__':
	main()
"""
#Dry run :
"""
	R_Factorial(5)
		5*4
			20*3
				60*2
					return 120
"""	
# Loop is faster and efficient than recursion
#	no caller, Callie , no register value updates , no stack  in loops so its faster
#	where as in recursion multiple frames get craeted in stack and every time multiple values needs to update. sp time consuming,memory inefficient.

#HW
# write a recursive program to find length of a string 
# write a recursive program to extract digits from string j789IN6236 = 7896236
# write a recursive program to count number of 1 bits in w/o using arithmetic operator