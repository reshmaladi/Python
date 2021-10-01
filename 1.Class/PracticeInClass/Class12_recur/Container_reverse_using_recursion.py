#!C:\Python34

def reversecontainer(x):
	
	if len(x)== 0:
		#print ("Inside string length zero")
		if type(x) == str:
		#	print ("When type is string")
			return x
		return list()
	y=reversecontainer(x[1:])
	if type(x) == str:
		#print ("Build recursion")
		return y+ x[0]
	y.append(x[0])
	return y


def main():
	
	x= [1,2,3,4,5]
	print ("before recursion", x)
	print (reversecontainer(x))
	x="India"
	print(reversecontainer(x))

if __name__=="__main__":
	main()