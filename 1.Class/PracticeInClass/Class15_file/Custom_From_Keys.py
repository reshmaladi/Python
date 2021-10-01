#!C:\Python34

def from_keys(input_dict, values=None):
	#print (input_dict, end= "\n")
	#print (values)
	result=dict()
	keys=input_dict.keys()
	#print ("keys from dictionary",keys)
	if type(values) == list:
		#print ("Inside list")
		i=0
		for key in keys:
			print (i, len(values))
			if i <len(values):
				result[key] = values[i]
				i+=1
				print (result[key], values[i])
				continue
			result[key] = None
	else:
		result= dict.from_keys(input_dict, values)
	return result
	

def main():
	input_dict = {1:1,2:2, 3:3}
	values= ["a", "b", "c"]
	from_keys(input_dict,values)
		
if __name__=="__main__":
	main()

	