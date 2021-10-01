#!C:\Python34

def assignvalues(l1,l2):
	print (l1, l2)
	details= {}
	for  i,val  in enumerate(l1):
		print ("I value", i)
		print ("value", val)
		#print (val)
		print (l2[i])
		key =val
		value = l2[i]
		#details[l1[i]] = l2[i]
		details.update (dict.fromkeys(key, value))
		print (details)
	


def main():
	l1= ["name", "age", "Occupation"]
	l2= ["Test1", "30", "Teacher"]
	assignvalues(l1,l2)
		
if __name__=="__main__":
	main()


