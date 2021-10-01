#!C:\Python34

def dictionary_of_char(sentence, cwd= "str"):
	if (cwd= "paragra
	
	result ={}
	for ch in sentence:
		if result.get(ch) != None:
			result[ch] +=1
		else: 
			result[ch] =1
	return result

def main():
	sentence = input("Enter your sentence")
	result = dictionary_of_char(sentence)
	print(result)
	#for ch in result:
		#print(result)
	
	
		
if __name__=="__main__":
	main()