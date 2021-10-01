#!C:\Python34

def dictionary_of_words(sentence):
	result ={}
	print (type(sentence))
	for ch in sentence.split():
		if result.get(ch) != None:
			result[ch] +=1
		else: 
			result[ch] =1
	return result

def main():
	sentence = input("Enter your paragraph")
	result = dictionary_of_words(sentence)
	print(result)
	
		
if __name__=="__main__":
	main()