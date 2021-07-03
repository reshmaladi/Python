#!C:\Python34
class bubble_sort:
	def __init__(self,nums):
		self.nums = nums
	
	def sort(self):
		for i in range(len(self.nums)-1):
			for j in range(len(self.nums)-i-1):
				if self.nums[j] < self.nums[j+1]:
					self.swap(j, j+1)
	
	def swap(self, i , j):
		self.nums[i] , self.nums[j] = self.nums[j] , self.nums[i]
		
		
if __name__ == "__main__":
	n = [2,5,1,6,3]
	s=bubble_sort(n)
	s.sort()
	print(s.nums)
