str1 = "abs"
str2 = "bacd"
char = 26

count1 = [0]*char
count2 = [0]*char
print(type(count1))
#print (count1, count2)

i=0
while i< len(str1):
#	print (ord(str1[i]))
	count1[ord(str1[i]) -ord('a')] +=1
	i+=1
	
print (count1)

j = 0
while j < len(str2):
	count2[ord(str2[j]) - ord('a')] +=1
	j +=1
	
print (count2)

cnt = 0
for i in range(26):
	cnt += abs(count1[i] - count2[i])
print ("needed removal ",cnt)
#print(type(cnt))
if (cnt > 2):
	print ("not posible")
else: print ("anagram")

'''
other approches are 
1  sorted (str1) == sorted(str2)
2. Counter(str1) == Counter(str2)
3  set(str1.lower()) == set(str2.lower())
'''