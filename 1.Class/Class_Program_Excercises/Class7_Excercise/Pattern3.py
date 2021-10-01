#!C:\Python34

def pattern1(num):
	for i in range(1, num +1):
		for _ in range(1, i+1 ):
			print (" ", end = "" )
		for _ in range(1,num-i+1):
			print ( "*" , end = "")
		print ("" , end= "\n")
		
def main():
	num= eval(input ("Enter your number of raws you want to print" ))
	pattern1(num)
		
if __name__=="__main__":
	main()
	
'''
Output
C:\>python C:\1.Class\Class_Program_Excercises\Class8_Excercise\Pattern3.py
Enter your number of raws you want to print6
 *****
  ****
   ***
    **
     *
'''