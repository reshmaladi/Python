#!C:\Python34
def logestsubstring(s):
	if len(s) <=1: return len(s)
	seen_char = {} # key value pair o store key as character and value as index for that character
	left = 0
	right = 0
	maximum_length = 0
	while(left < len(s) and right <len(s)):
		el = s[right]											#el = a			el=b
		if (el in seen_char):
			print("seen_char[el] and el are ", seen_char[el], el)
			left = max(left, seen_char[el] + 1)					# 
		seen_char[el] = right									# a = 0 
		maximum_length = max(maximum_length, right-left + 1)	#max(0,0-0+1) =1
		right +=1												# right = 1
	return maximum_length




'''
def logestsubstring(s):
	if len(s) <=1: return len(s)
	seen_char = {} # key value pair o store key as character and value as index for that character
	left = 0
	logest = 0
	for right in range(0, len(s)):
		current_char = s[right]
		pre_seen_char = seen_char.get(current_char)
		#print ("TTT",pre_seen_char)
		if(pre_seen_char >=left):
			left = pre_seen_char +1
		seen_char[current_char] = right
		logest = max(logest,right-left +1)

		print (logest)
	return logest
'''
s= "abcdeeft"
print(logestsubstring(s))