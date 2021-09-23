"""
Write a program, preferably in Python that, given a text-file, counts the number of words and reports the top N words ordered by the number of times they appear in the file.
"""
N = int(input("How many words to print: "))
word_freq = {}			# Dictionary {word: occurance count}

path = "C:\\Users\\reshma.ladi\\Documents\\GitHub\\Python\\selfpractice\\"
with open(path +"test.txt", "r") as fp:
	content = fp.read()
	words = content.split()
#Create dictionary , with key as word in file and value as frequency of occurrence in file
for item in words:
	if item in word_freq:
		word_freq[item] += 1
	else:
		word_freq[item] = 1
# sorted above dictionary by value and return element as per request
print(list(sorted(word_freq.items(), key=lambda x:x[1], reverse = True))[:N])

#for x,y in sorted(d_2.items(), reverse = True)[:20]:
#sorted(my_dict.items(), key=operator.itemgetter(1))[:5]
#sorted_x = sorted(freq.items(), key=operator.itemgetter(1))
#wordcnt = sorted(freq.items(), key=lambda x:x[1])
#print (str(wordcnt))
'''
marklist=sorted((value, key) sue h)
sortdict=dict([(k,v) for v,k in sorted_dt])
print("sort ,",sortdict)
'''
#print(sorted_x)

