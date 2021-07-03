#!C:\Python34
class selection_sort():
	def __init__(self, nums):
		self.nums = nums
	
	def sorting(self):
		for i in range(len(self.nums)):
			min = i
			print ("Minimum" , min,self.nums[min])
			print ("Outer loop +++++++++++", i)
			for j in range(i, len(self.nums)):
				print("Inner j",j)
				if self.nums[j] < self.nums[min]:
					min =j
					print ("Minimum after swap", min, self.nums[min])
					
			if min != i:
				self.nums[min],self.nums[i] = self.nums[i], self.nums[min]
				
if __name__ == "__main__":
	n = [3,4,6,1,8,0]
	s= selection_sort(n)
	s.sorting()
	print(s.nums)