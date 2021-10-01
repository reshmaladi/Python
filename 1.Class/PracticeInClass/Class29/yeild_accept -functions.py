

def InitWrapper(func):
	def Init():
		data=func()
		next(data)
		return data
	return Init

@InitWrapper
def increament():
	x=yield
	yield x+10



	
def main():
	'''
	init = InitWrapper(increament)
	data= init()
	print (data.send(50))
    '''
	data = increament()
	print (data.send(50))
if __name__ == "__main__":
    main()
