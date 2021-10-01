#!C:\Python34

def swapbits(x,y,posx,posy, bits):
	
	print (" original x  ", '{0:08b}'.format(x), end = "\n")
	print (" original y  ", '{0:08b}'.format(y), end = "\n")
	#print mask for x
	x_mask=(1<<bits)-1
	print (" mask  ", '{0:08b}'.format(x_mask), end = "\n")
	x_mask=x_mask<<(posx-bits)
	print (" mask after bits shift   ", '{0:08b}'.format(x_mask), end = "\n")
	
	#print mask for y
	y_mask=(1<<bits)-1
	print (" mask  ", '{0:08b}'.format(y_mask), end = "\n")
	y_mask=y_mask<<(posy-bits)
	print (" mask after bits shift   ", '{0:08b}'.format(y_mask), end = "\n")
	
	#Create x_part and y_part 
	x_part = x & x_mask
	print (" x_part   ", '{0:08b}'.format(x_part), end = "\n")
	y_part = y & y_mask
	print (" y_part  ", '{0:08b}'.format(y_part), end = "\n")
	
	
	if (posx > posy):   						#If x position is greater than y position 
		x_part = x_part >> (posx - posy)
		y_part = y_part << (posx - posy)
	else:										#If y position is greater than y position 
		x_part = x_part >> (posx - posy)
		y_part = y_part << (posx - posy)
		
	x= x & ~x_mask
	y= y & ~y_mask
	
	
	x= x | y_part
	print (" x   ", '{0:08b}'.format(x), end = "\n")
	y= y | x_part 
	print (" y  ", '{0:08b}'.format(x), end = "\n")
	return x, y
	
	
def main():
	x = eval(input ("Enter your first number" ))
	y = eval(input ("Enter your second number" ))
	posx = eval(input ("Enter your position " ))
	posy = eval(input ("Enter your position " ))
	bits = eval(input ("Enter your bits" ))
	a, b= (swapbits(x, y, posx, posy, bits))
	print (a, b)	
	
if __name__=="__main__":
	main()
	
	

	
	