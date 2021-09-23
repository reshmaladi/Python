class Solution:
    def longestOnes(self, A, K) :
        left, right = 0, 0
        num0 = 0
        ret = 0
        while right < len(A):
            while num0 <= K and right < len(A):
                if A[right] == 0:
                    num0 += 1
                right += 1
            
            if num0 > K:
                ret = max(ret, right - left - 1)
            else:
                ret = max(ret, right - left)
            while num0 > K and left < right:
                if A[left] == 0:
                    num0 -= 1
                left += 1
        return ret
		
s= Solution()
k =s.longestOnes([0,0,1,1,0,1],2)
print(k)