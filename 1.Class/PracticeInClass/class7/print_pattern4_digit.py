#!C:\Python34

def pattern2(n):
	
	for i in (range(1, n+1)):
		for _ in (range(1 , n-i+1)):	
			print( " " , end = "" )
		count=i
		
		for j in (range(1 , i*2)): ## (1 , 2) (
			print ( count , end= "")
			if j < i: 
				count =count -1
				
			else:
				count = count +1
				
		print( "" , end = "\n" )
		
def main():
	num  = int( input ("Enter the number "))
	pattern2(num)


if __name__=="__main__":
	main()


	
'''

   1
  212
 32123
4321234

Logic for the program 

1st iteration 
i=1
 first for loop  range (1, 4 -1+1) which is [1,4]  will create list as [1,2,3]
 second for loop range (1, 1+1) which is [1,2]	>> will create list as [1]
 
2st iteration 
i=2
 first for loop  range (1, 4-2+1) which is [1,3]  will create list as [1,2]
 second for loop range (1, 2+1) which is [1,3]	>> will create list as [1,2]

3st iteration 
i=3
 first for loop  range (1, 4-3+1) which is [1,2]  will create list as [1]
 second for loop range (1, 3+1) which is [1,4]	>> will create list as [1, 2, 3]

4st iteration 
i=4
 first for loop  range (1,4-4+1) which is [1,1]  will create list as [0]
 second for loop range (1, 4+1) which is [1,5]	>> will create list as [1,2,3,4]

	
	
	
	
	
	
'''