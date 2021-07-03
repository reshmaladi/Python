#Open file 
# counter =0 
# dict = {}
#for loop on line with space separation
#add counter + 1 per word 

text = open("temp_file.txt", r)
d = {}
for line in text:
	line = line.strip()
	line = line.lower()
	words = line.split()
	for w in words:
		if w in d:
			d[w] = d[w] +1
		else:
			d[w] = 1


