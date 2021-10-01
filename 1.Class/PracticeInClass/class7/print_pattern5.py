#!C:\Python34

def pattern1(num):
	n = 0
	for i in range(1, num +1):
		for _ in range(1, num-i+1 ):
			print ("*" , end = "" )
		# loop to print star 
		while n != (2 * i - 1): 
			print(" ", end = "") 
			n = n + 1
		n=0         
		print ("" , end= "\n")
		
		
		
def main():
	num= eval(input ("Enter your number of raws you want to print" ))
	pattern1(num)
		
if __name__=="__main__":
	main()