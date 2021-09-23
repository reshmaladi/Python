def feb(limit):
	a,b =0,1
	
	while a<limit:
		yield a
		a,b = b, a+b		
		
x=feb(5)
print(list(x))