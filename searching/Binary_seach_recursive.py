#!C:\Python34
def BinarySearch(array, element, start, end):
	step =0
	if start > end :
		return -1
	mid = (start + end) // 2
	
	if element == array[mid]:
		return mid
	if element < array[mid]:
		print("Sub Array", array[start: mid-1])
		return BinarySearch(array, element , start , mid-1)
	else :
		step = step +1
		print("Sub Array ",  array[mid+1: end])
		return BinarySearch(array, element, mid+1, end)

array = [ 1,2,4,6,8,9,10, 14, 20, 24, 30]
element = 6
print (BinarySearch(array, element,0, len(array)))