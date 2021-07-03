def highestSum(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    # n must not be smaller than k
    if n < k:
        return -1

    # Compute sum of first window of size k
    window_sum = sum([arr[i] for i in range(k)])

    # Compute sums of remaining windows by 
    # removing first element of previous 
    # window and adding last element of 
    # current window. 
    print(window_sum)
    for i in range(n - k):
        print("Elements involved are ", arr[i] , arr[i + k], "And value of i ", i)
        window_sum = window_sum - arr[i] + arr[i + k]
        print ("Latest calculated sum is ", window_sum)
        highest_sum = max(highest_sum, window_sum)

    return highest_sum

arr= [1,5,2,3,6,3,8,2]
print (highestSum(arr,3))