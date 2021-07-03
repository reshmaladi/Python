def highestSum(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    # n must be not smaller than k
    if n < k:
        return -1

    left = 0
    right = 0
    window_sum = 0
    while right < n:
        # sliding the window to the right
        window_sum += arr[right]
        right += 1

        # check the window size condition and compare the sum
        # drop off the left element to avoid oversize
        if right-left == k:
            highest_sum = max(highest_sum, window_sum)
            window_sum -= arr[left]
            left += 1

    return highest_sum
	
arr= [1,5,2,3,6,3,8,2]
print (highestSum(arr,3))