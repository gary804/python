def hasDuplicate(*array):
	print array	#it become Tuple
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i] == array[j]:
				return True
	return False

#a = [1,2,3,8,4,5,6,7,8,9]	# works
a = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,17)	# works
print hasDuplicate(*a)

def binary_search(ai, *array):
	print array, ai
	al = len(array)
	p = al/2
	hl1,hl2= 0, p-1
	hh1,hh2= p+1, al-1
	while(True):
		print "(", p, hl1,hl2,hh1,hh2, ")"
		if ai == array[p]:
			return "Index is: " + repr(p)
		else:
			if ai > array[p]:
				if (hh2-hh1>1 ):
					p= hh1+(hh2-hh1)/2
					hl1 = hh1
					hl2 = p-1
					hh1 = p+1
					hh2 = hh2
				else:
					for j in range(hh2-hh1+1):
						print hh1+j,
						if (ai == array[hh1+j]):
							return "Index is: " + repr(hh1+j)
					return "Index is: -1"
			else:
				if (hl2-hl1>1):
					p=hl1+(hl2-hl1)/2
					hh2 = hl2
					hh1 = p+1
					hl1 = hl1
					hl2 = p-1
				else:
					for j in range(hl2-hl1+1):
						print hl1+j,
						if (ai == array[hl1+j]):
							return "Index is: " + repr(hl1+j)
					return "Index is: -1"

def binary_search1(ai, *array):
	print array, ai
	al = len(array)
	p = al/2
	hl1,hl2= 0, p-1
	hh1,hh2= p+1, al-1
	while(True):
		print "(", p, hl1,hl2,hh1,hh2, ")"
		if ai == array[p]:
			return "Index is: " + repr(p)
		else:
			if ai > array[p]:
				if (hh2-hh1>1 ):
					p= hh1+(hh2-hh1)/2
					hl1 = hh1
					hl2 = p-1
					hh1 = p+1
					hh2 = hh2
				else:
					if (ai == array[hh1]):
						return "Index is: " + repr(hh1)
					elif (ai == array[hh2]):
						return "Index is: " + repr(hh2)
					else:
						return "Index is: -1"
			else:
				if (hl2-hl1>1):
					p=hl1+(hl2-hl1)/2
					hh2 = hl2
					hh1 = p+1
					hl1 = hl1
					hl2 = p-1
				else:
					if (ai == array[hl1]):
						return "Index is: " + repr(hl1)
					elif (ai == array[hl2]):
						return "Index is: " + repr(hl2)
					else:
						return "Index is: -1"


a = list(a)
a.sort()
for i in range(-1,len(a)+2):
	print binary_search(i, *a)

