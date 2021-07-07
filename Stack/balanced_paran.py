#!C:\Python34
def balance_check(s):
	#print(s)
	if len(s) %2 != 0: 
		return False
		
	opening = set('([{')
	matches = set([( '(', ')' ), ( '[' , ']' ), ( '{', '}')])    # List of tuples of all pairs
	
	# implementing list as stack . Usebuilt in funstions of list
	
	stack =[]
	for param in s:						#scaning string from left t right
		if param in opening:			# If we see any opening parenthesis we put that in stack 
			stack.append(param)
			print("After append",stack)
		else:
			if len(stack) == 0:			#
				return False
			last_open = stack.pop()
			print("Last open", last_open)
			print ("After poping out", stack)
						
			#Check if there is closing match
			print ("#####3",last_open, param)
			if (last_open, param) not in matches:
				return False
				
	return len(stack) == 0
	
	#print(balance_check('[]'))
print(balance_check('[]({}}'))
	
	