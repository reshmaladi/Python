#!C:\Python34
def main():
	fd = open("C:\\1.Class\\Class_Program_Excercises\\Class16_Excercise\\audio.conf")	
	
	if fd != None:
		line = fd.readline()
		conf ={}
		conf1= {}
		while line != "":
			
			line = fd.readline()
			if (line.startswith("#")  or line.startswith("\n")):
				continue
			
			elif line.startswith("["):
				key1= line
				print ("Ouuter key is \n ", key1, "\n")
				key1!="":
					conf.update({key1 : conf1})
			
			else:
			
				if (line.startswith("[")) == False:
					#line = fd.readline()
										
					if ":" in line: 
						key = line.rpartition(":")[0]
						value = line.rpartition(":")[2]
						value =value.strip("\n")
						if "#" in value:
							value = line.rpartition("#")[0]
						conf.update({key : value})
					elif "=" in line:
						key = line.rpartition("=")[0]
						value = line.rpartition("=")[2]
						value =value.strip("\n")
						if "#" in value:
							value = line.rpartition("#")[0]
					
						conf.update({key : value})
					print ("Inner dictionary is \n", conf)
			conf1.update({key1: conf})
		
		print ("Final dictionary : ", conf1)
				
if __name__=="__main__":
	main()