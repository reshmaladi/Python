#!C:\Python34

def insertion_sort(nums):
	for i in range (len(nums)):
		j=i
	
		while (j > 0 )and (nums[j-1] > nums[j]):
			nums[j-1], nums[j] = nums[j], nums[j-1]
			j=j-1
		
if __name__=="__main__":
	n= [2,41,5,18,45,88,-1]
	insertion_sort(n)
	print(n)
	
	