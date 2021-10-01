def factorial(no):
	if(no==0):
		return no
	if(no==1):
		return no
	fact=1
	for x in range (1, no+1):
		fact =fact* x
	return fact
		
#no =  eval(input ("enter use from n "))
f= factorial(5)
print (f)