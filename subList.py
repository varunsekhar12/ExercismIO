def getSublist(l,s):
	sub_l = False
	if s == []:
		sub_l = True
	elif s == l:
		sub_l = True
	elif len(s) > len(l):
		sub_l = False
	else:
		for i in range(len(l)):
			if l[i]==s[0]:
				n=1
				while(n < len(s)) and (l[i+n] == s[n]):
					n+= 1
			    	if n == len(s):
						sub_l = True
	return sub_l

a = [1,2,3,4,5]
b = [2,3]
c = [4,5]
print(getSublist(a, b))
print(getSublist(a, c))
