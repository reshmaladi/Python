#!C:\Python34\
# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    else: return False

def isPalindromenumber(no):
	ret = 0
	rev =0
	while no != 0 : 
		rem =no% 10
		rev = rev * 10 + rem 
		no = int (no //10 )
	return rev
  
def main():	
    s = "12321"
    ans = isPalindromenumber(s)
    c = "abcba"
    ans = isPalindrome(s)
    if ans == 1: 
        print("Yes") 
    else: 
        print("No")

if __name__=="__main__":
	main()

