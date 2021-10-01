#!C:\Python34

def storopt(s1):
	
	#for i in range(len(s1)):
		count=1
		cur =s1[0]
		for j in range(len(s1)):
			print (s1[j+1] , s1[j])
			if (s1[j] == s1[j+1]): 
				count = count +1
			else: 
				cur = s1[j+1]
				count = 1
				
		print ("count is ", count)

def main():
	s1 = str(input ("enter the number"))
	print (storopt(s1))
	
if __name__=="__main__":
	main()