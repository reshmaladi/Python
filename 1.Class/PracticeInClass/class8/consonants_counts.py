#!C:\Python34
# Print consonant counts
def consonant_counts(userinput):
	voval= ('a','e','i','o', 'u', 'A', 'E', 'I', 'O', 'U' )
	count =0 
	for x in userinput:
		if x in voval:
			continue 
		count  = count +1
	return count

def main():
	input1= input ("Enter string")
	print (input1)
	print (consonant_counts(input1))
	
if __name__=="__main__":
	main()

