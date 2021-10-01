#!C:\Python34
def Menu():
	while True:
		print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
		choice=eval(input("Enter your choice"))
		#print (choice)
		if(choice>0 or choice<=6):
			return choice

def ArithmaticOperations():
	choice=0
	while(choice!=5):
		choice=Menu()
		if(choice==1):
			number1=eval(input("Enter first Number :"))
			number2=eval(input("Enter second Number :"))
			addition=number1+number2
			print( addition)
		elif(choice==2):
			number1=eval(input("Enter first Number :"))
			number2=eval(input("Enter second Number :"))
			sub=number1-number2
			print( sub)
		elif(choice==3):
			number1=eval(input("Enter first Number :"))
			number2=eval(input("Enter second Number :"))
			multiply=number1*number2
			print (multiply)
		elif(choice==4):
			number1=eval(input("Enter first Number :"))
			number2=eval(input("Enter second Number :"))
			divide=number1/number2
			print (divide)
def main():
	ArithmaticOperations()

	
if __name__=="__main__":
	main()

	




