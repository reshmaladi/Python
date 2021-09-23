def first_position(s):
	s2 = ''
	s = str(s)
	for i in range(0,len(s)):
		if s[i] not in s2:
			print('First position of {} is {}'.format(s[i],i))
			s2 = s2 + s[i]
			
first_position(10122334455887667)

exit()