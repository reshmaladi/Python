#!C:\Python34

def swapbits(x,y,pos, bits):
	
	print (" original x  ", '{0:08b}'.format(x), end = "\n")
	print (" original y  ", '{0:08b}'.format(y), end = "\n")
	
	
	mask=(1<<bits)-1
	print (" mask  ", '{0:08b}'.format(mask), end = "\n")
	mask=mask<<(pos-bits)
	print (" mask after bits shift   ", '{0:08b}'.format(mask), end = "\n")
	x_part = x & mask
	print (" x_part   ", '{0:08b}'.format(x_part), end = "\n")
	y_part = y & mask
	print (" y_part  ", '{0:08b}'.format(y_part), end = "\n")
	
	
	x= x & ~mask
	y= y & ~mask
	
	
	x= x | y_part
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	y= y | x_part 
	print (" y  ", '{0:08b}'.format(x), end = "\n")
	return x, y
	
	
def main():
	x = eval(input ("Enter your first number" ))
	y = eval(input ("Enter your second number" ))
	pos = eval(input ("Enter your position " ))
	bits = eval(input ("Enter your bits" ))
	a, b= (swapbits(x, y, pos, bits))
	print (a, b)	
	
if __name__=="__main__":
	main()
	
	

	
	