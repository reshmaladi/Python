#!C:\Python34
def large_cont_sum(arr):
	#arr = [2, 3, 2, 4, 3, 5,1,2]
	print(*arr)
	if len(arr) == 0 :			# first check if length of array is not 0
		return 0
		
	max_sum = current_sum =arr[0]
	
	for num in arr[1:]:		#Navigate to each element in arrary
		#print (num)
		current_sum  =max(current_sum +num , num)		#max(1+2, 2)
		print ("current_sum", current_sum)
		max_sum = max(current_sum , max_sum) #(3,1)
		print("max_sum",max_sum)
	return max_sum 
	
print(large_cont_sum([2, 3, 2, -4, 3, 5,-1,2]))
#large_cont_sum([2, 3, 2, 4, 3, 5,1,2])