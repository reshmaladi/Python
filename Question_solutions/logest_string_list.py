fruits = ["Apple", "Mongo", "banana","Pinapple", "lichi"]
max_length = 0
for st in fruits :
	if len(st) >= max_length:
		max_length = len(st)
		res= st
print (res)