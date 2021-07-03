def highestSum(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    # n must not be smaller than k
    if n < k:
        return -1

    # subarray starts at i
    for i in range(n - k + 1):
        # calculate sum of the subarray
        current_sum = 0
        for j in range(k):
            print("Value fo i and j are :", i, j, "#####")
            current_sum += arr[i + j]
        # compare the sum
        highest_sum = max(highest_sum, current_sum)
    return highest_sum

arr= [1,5,2,3,6,3,8,2]
print (highestSum(arr,3))