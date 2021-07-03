#!C:\Python34
x = "ABC"
y = "ABC"

if len(x) != len(y):
	print("Not anagram")

mapx = {}
for i in range(len(x)):
	mapx[x[i]] = mapx.get((x[i]) , 0) + 1
for k, v in mapx.items():
	print( k, v)

mapy = {}
for j in range(len(y)):
	mapy[y[j]] = mapy.get((y[j]) , 0) + 1

for k, v in mapy.items():
	print( k, v)
	
if mapx == mapy:
	print ("Anagram")
	
else: 
	print("Not Anangram")
	
	
if sorted(x) == sorted(y):
	print("Ana")
else: ("not ana")


