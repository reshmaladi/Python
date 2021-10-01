#!C:\Python34

def main():
	fd = open("C:\\1.Class\\Class_Program_Excercises\\Class16_Excercise\\audio.conf")	
	
	if fd != None:
		line = fd.readline()
		conf ={}
		conf1= {}
		key1="";
		while line != "":
			
			line = fd.readline()
			if (line.startswith("#")  or line.startswith("\n")):
				continue
				print (line)
			elif line.startswith("["):
				if key1!="":
					conf.update({key1 : conf1})
					key1="";
					conf1={};
					
				key = line
				key1=key
				print ("outerkey is :" ,key)
				
				
			else:
				key = line
				print ("outerkey1 is :" ,key)
				
				print 
				if "=" in line: 
					print ("my line is ", line)
					key = line.rpartition("=")[0]
					value = line.rpartition("=")[2]
					value =value.strip("\n")
					if "#" in value:
						value = line.rpartition("#")[0]
					print ("key", key, "value" , value)
					conf1.update({key : value})
			if key1!="":
					conf.update({key1 : conf1})
			print (conf)
			'''
			for l in line:
				if (line.startswith("[")) == True:
					#l1 = fd.readline()
					print ("l1 is ", line)
			'''
					
					
				
				
		


if __name__=="__main__":
	main()