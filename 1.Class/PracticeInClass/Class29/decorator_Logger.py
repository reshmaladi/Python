

def LogDecorator(func):
	def Init():
		data=func()
		next(data)
		return data
	return Init

@InitWrapper
def increament():
	x=yield
	yield x.upper()
	
	
def main():
	user_string = "learning python"
	data = increament()
	print (data.send(user_string))
if __name__ == "__main__":
    main()
