#!C:\Python34

def Menu():
    while True:
        print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
        choice=eval(input("Enter your choice"))
		#print (choice)
        if(choice>0 or choice<=6):
              return choice
			  

def pop(x):
	x.pop()
	
def push(x,el):
	x.append(el)
def pip(x):
	return x[-1]
def isfull(x):
	return len(x)==10

def isempty(x):
	return len(x)==0

def main():
	x=[1,2,4,3,6,5,7]
	print ("Please enter the options from manu to perform operation,  (x) to exit " 
			1. pop  
			2. Push 
			3. IsEmpty 
			4. IsFull 
			5. X to exit , end= " \n")
	el= eval(input("enter number you want to perform"))
	if(ch==1):
		pop(x)
	if(ch==2):
		el=eval(input("enter element to enter"))
		push(x,el)
	if(ch==3):
		isempty()
	if(ch==4):
		isfull()
	

if __name__=="__main__":
	main()