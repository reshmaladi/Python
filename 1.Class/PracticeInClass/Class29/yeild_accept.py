
def init(data):
	next(data)

def increament():
	x=yield
	yield x+10

	
def main():
	data =increament()
	#next(data)
	init(data)		# We can also initialize by writing new function to initialize the value 
	#data.send(None)   # Yield should be either initialize with None or with data 
	print(data.send(10))
   
if __name__ == "__main__":
    main()
