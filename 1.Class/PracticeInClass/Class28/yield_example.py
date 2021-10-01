#!C:\Python34
def YieldDemo():
	i=0
	
	for i in range(10):
		yield (i)
		
		
x = YieldDemo()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


##Iterator with yild is generator