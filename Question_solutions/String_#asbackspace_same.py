#!C:\Python34
def build_string(s,t):
	p1 = len(s)-1
	p2 = len(t)-1
	while(p1>=0 or p2 >= 0):
		if(p1 == '#' or p2 == '#'):
			print("Inside first if")
			if(p1 == '#'):
				backcount = 2
				while(backcount >0):
					p1 -=1
					backcount -=1
					if(s[p1] == '#'):
						backcount = backcount + 2
			if(p2 == '#'):
				backcount = 2
				while(backcount >0):
					p2 -=1
					backcount -=1
					if(t[p2] == '#'):
						backcount = backcount + 2
		else:
			print(s[p1] ,t[p2])
			if(s[p1] != t[p2]):
				return False
			else:
				p1-=1
				p2-=1
	return True
	
if __name__=="__main__":
	s="abc#d"
	t="abzz##d"
	print(build_string(s,t))