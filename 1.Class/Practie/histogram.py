def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])



#!C:\Python34
num  = input ("Enter the sentence ")
#numbers = list(map(int, a.split()))
print (list (num))
for n in (list (num)):
#[int(x) for x in str(num)]
	output = ''
	times = int( n)
	while( times > 0 ):
		output += '*'
		times = times - 1
	print(output)