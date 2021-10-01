#!/usr/bin/python
class SpeedLimitError(Exception):
	"""Base Class for User definded Exception"""
	def __inti__(self, speed):
		self.speed =speed
	def __str__(self):
		return "Speed is "+str(self.speed)
	
class SpeedBelowLimit(SpeedLimitError):
	"""Speed below Limit Execption"""
	def __init__(self, speed):
		SpeedLimitError.__init__(self,speed)

class SpeedAboveLimit(SpeedLimitError):
	"""Speed above Limit Execption"""
	def __init__(self, speed):
		SpeedLimitError.__init__(self,speed)
		
def main():
	while True:
		try:
			speed = eval(input("Enter Speed"))
			if speed>80:
				x = SpeedAboveLimit(speed)
				raise x
			elif speed<20:
				raise SpeedBelowLimit(speed)
			else:
				print("Speed In limit")
				break
		except SpeedAboveLimit as e:
			print(e,"is SpeedAboveLimit")
		
		except SpeedBelowLimit as e:
			print(e,"is SpeedBelowLimit")
		
		finally:
			print("COOL")
		
if __name__=="__main__":
	main()
