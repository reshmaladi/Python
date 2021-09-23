class solution:
	def typewords(self, sent, broken):
		s =set (broken)
		count = 0
		for word in (sent.split(" ")):
			if all(c not in s for c in word):
			 count +=1
			 print (word)
		return count
			
s= solution()
print(s.typewords("Hello word","l"))