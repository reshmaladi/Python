#!C:\Python34\
# Python program to check 
# if a string is palindrome  
# or not 
  
x = "malayalam"
w = "" 
for i in x: 
	print ("i is " + i)
	w = i + w 
	print ("w is " +  w)
	if (x==w): 
		print("YES") 
    