#!C:\Python34
def upper_lower_count(sentence):
	result= {"lower" :  0, "upper" : 0}
	for ch in sentence.split():
		if ch.islower():
			result["lower"] +=1
		elif ch.isupper():
			result["upper"] +=1
	return result


def main():
	sentence = input("Enter sentence ")
	result = upper_lower_count(sentence)
	print(result)

		
if __name__=="__main__":
	main()