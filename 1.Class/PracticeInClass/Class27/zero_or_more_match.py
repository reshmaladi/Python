#!C:\Python34
import re
#re.search("a* , 'babababaaaaba')
#for match in re.finditer('a{1,3}' , 'babababaaaaba'): 
#for match in re.finditer('a[1][2]' , 'ba12ba1ba3baaaa4ba5'):  # it becomes set and mathes for each element 
#for match in re.finditer('[^a-zA-Z0-9]+' , '@!@#babababaaaaba'): #  Negation of alphanumeric 
for match in re.finditer('a|b' , 'babababaaaaba'): 

	print(match)