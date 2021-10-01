#!C:\Python34

def recursive_length(x):
	count =0
	if x=="" : return 0
	if x:
		#count =count+1 
		#x =x -1
		return 1+ recursive_length(x[1:])
	
def main():
	x= str(input("enter first number"))
	#y= eval(input("enter second number"))
	print (recursive_length(x))

if __name__=="__main__":
	main()
	
	
'''
count =0
while x[count]!="":
	count +=1
	
'''