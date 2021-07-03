#!C:\Python34
def BinarySearch(array, element):
	start = 0
	mid = 0
	end = len(array)
	step = 0
	while(start<=end):
		print ("Subarray in step {}: {}" .format(step, str(array[start:end+1])))
		step =step + 1
		mid = (start + end ) //2
		print ("Got mid as :", mid)
		print("Mid element is", array[mid])
		if element == array[mid]:
			return mid
		if element < array[mid] :
			end = mid - 1
		else:
			start = mid + 1
	return -1

array = [ 1,2,4,6,8,9,10, 14, 20, 24, 30]
element = 24
print (BinarySearch(array, element))