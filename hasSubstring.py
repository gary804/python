import cProfile

def hasSubstring0(mainstring, substring):
	for i in range(len(mainstring)):
		print i
		for j in range(len(substring)):
			print j
			if i+j>=len(mainstring):
				return False
			if mainstring[i+j]!=substring[j]:
				break
		if j== len(substring)-1 and mainstring[i+j]==substring[j]:
			return True
	return False

def hasSubstring1(mainstring, substring):
	for i in range(len(mainstring)-len(substring)+1):
		print i
		for j in range(len(substring)):
			print j
			#if i+j>=len(mainstring):
			#	return False
			if mainstring[i+j]!=substring[j]:
				break
		if j== len(substring)-1 and mainstring[i+j]==substring[j]:
			return True
	return False

def hasSubstring1_1(mainstring, substring):
	ml, sl =len(mainstring), len(substring)
	srange=range(sl)
	for i in range(ml-sl+1):
		print i
		#for j in range(sl):
		for j in srange:
			print j
			#if i+j>=len(mainstring):
			#	return False
			if mainstring[i+j]!=substring[j]:
				break
		if j== sl-1 and mainstring[i+j]==substring[j]:
			return True
	return False

def hasSubstring2(mainstring, substring):
	i, j=0,0
	ml, sl = len(mainstring), len(substring)
	while i < ml:
		#print i
		#print j
		if mainstring[i]!=substring[i-j]:
			if i==j: j, i= i+1, i+1
			else: j=i
		else:
			i +=1
			if i-j== sl:
				return True
	return False

#print hasSubstring('babate', 'bate')
#print hasSubstring('babate', 'batez')
#print hasSubstring('babate', 'babate')
cProfile.runctx("print hasSubstring2('bzztzzz', 'a')",globals(),locals())
cProfile.runctx("print hasSubstring1_1('babate', 'bat')",globals(),locals())
cProfile.runctx("print hasSubstring1_1('babbate', 'bat')",globals(),locals())