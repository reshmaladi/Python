def palindrome_with_space(s):
    s = s.replace(' ','') # To remove space
    for i in range(0,len(s)):
        print ( -i-1)
        if s[i] != s[-i-1]:
            print('Not Palindorme')
            break
    else:
        print('Palinrome')

		
print(palindrome_with_space('helleh'))