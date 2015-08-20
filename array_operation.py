#!/usr/bin/python

#def hasDuplicate(*array):
def hasDuplicate(array=[]):
	print array	#it become Tuple
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i] == array[j]:
				return True
	return False

#a = [1,2,3,8,4,5,6,7,8,9]	# works
a = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,17)	# works
#print hasDuplicate(*a)	#for def hasDuplicate(*array):
print hasDuplicate(a)

#def binary_search(ai, *array):
def binary_search(ai, array=[]):
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

#def binary_search1(ai, *array):	#it works, but not good, the *array is for variable arguments
def binary_search1(ai, array=[]):
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
print '====================================================================='
for i in range(-1,len(a)+2):
	print binary_search(i, a)
print '====================================================================='

def atoi(str):
	digit = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	integer = 0
	sign = 1
	for i in range(len(str)):
		if (str[i] == '-'):
			sign = -sign
		elif (str[i]=='+'):
			continue
		elif (str[i]=='.'):
			break
		elif (str[i]>='0' and str[i]<='9'):
			integer = integer * 10 + digit[str[i]]
		else:
			return 0
	return integer * sign

str = '+1234'
str1 = '-1234.5'
str2 = '123a45'
print '{0} is {1}, {2} is {3}, {4} is {5}'. format (repr(str), atoi(str), repr(str1), atoi(str1), repr(str2), atoi(str2))

#from string import *   # to use split(string)
def reverse_words(string):
	#wlist = split(string)  #this split() must be imported
	wlist = string.split()
	wllast = len(wlist) - 1
	for i in range(len(wlist)/2):
		tem = wlist[i]
		wlist[i] = wlist[wllast-i]
		wlist[wllast-i] = tem
	return ' '.join(wlist)

string = 'Write a function to reverse the order of words in a string in place.'
print reverse_words(string)

def reverse_characters(string):
	clist = list(string)
	clist.reverse()
	return ''.join(clist)

def reverse_words_characters(string):
	#wlist = split(string)  #this split() must be imported
	wlist = string.split()
	wllast = len(wlist) - 1
	for i in range(len(wlist)/2):
		tem = wlist[i]
		wlist[i] = reverse_characters(wlist[wllast-i])
		wlist[wllast-i] = reverse_characters(tem)
	return ' '.join(wlist)

print reverse_words_characters(string)

def merge(arg1=[], arg2=[]):	#works, its default is the empty list
#def merge(arg1, arg2):	#works
	l = len(arg1)+len(arg2);
	i1=0; i2=0;
	list1 = [];
	for i in range(l):
		if (i1<len(arg1) and i2<len(arg2)):
			if (arg1[i1]<arg2[i2]):
				list1.append(arg1[i1])
				i1+=1
			else:
				list1.append(arg2[i2])
				i2+=1
		elif (i1<len(arg1)):
			list1.append(arg1[i1])
			i1+=1
		else:
			list1.append(arg2[i2])
			i2+=1
	return list1
print "mergeTesting:"
l1=[1,3,5,7,9]
l2= [0,2,4,6,8]
l3 = merge(l1, l2)
print l3

def mergeSort(array=[]):
	if len(array)==1:
		return array
	l = len(array)/2
	a1 = mergeSort(array[0:l])
	a2 = mergeSort(array[l:])
	a3 = merge(a1, a2)
	return a3

def mergeSortIterate(array=[]):
	k =1
	while(k<=len(array)/2):
		i=0
		#print array, "k=", k
		while(i<len(array)):
			if i+k >=len(array):
				break
			wend=i+2*k
			if wend>len(array):
				wend= len(array)
			a1 = array[i:i+k]
			a2 = array[i+k:wend]
			a3 = merge(a1, a2)
			for j in range(wend-i):
				array[i+j]=a3[j]

			i=i+2*k
		k = k*2
		#print array
	a1 = array[:k]
	a2 = array[k:]
	a3 = merge(a1,a2)
	return a3

print "mergeSortTesting:"
l4 = [0,8,2,10,6,14,4,12,1,11,9,3,15,7,5,13]
#l5 = mergeSortIterate(l4)
import cProfile
#cProfile.run('l5 = mergeSortIterate(l4)')
cProfile.run('l5 = mergeSort(l4)')

print l5,l4
l4 = [0,8,2,6,10,14,4,12,1,11,9,3,7,5,13]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,10,12,1,11,9,3,7,5,13]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,12,10,1,11,9,3,7,5]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,1,11,9,10,3,7,5]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,1,9,3,7,5,10]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,1,9,3,7]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,1,9,3,]
l5 = mergeSortIterate(l4)
print l5,l4
l4 = [0,8,2,6,4,1,9]
l5 = mergeSortIterate(l4)
print l5,l4

def quickSort(array, startIndex, endIndex):
	pivot = array[startIndex+(endIndex - startIndex)/2]
	i = startIndex
	j = endIndex
	temp = 0
	#print "---------------------------------------------------------"
	#print "s=", startIndex, ",e=", endIndex, ",pivot=", pivot, array
	if ( (endIndex - startIndex) == 1):
		if ( array[startIndex] > array[endIndex] ):
			temp = array[startIndex]
			array[startIndex] = array[endIndex]
			array[endIndex] = temp
		return
	while(i<j):
		while(array[i]<pivot):
			i+=1
		while(array[j]>pivot):
			j-=1
		if (i>=j):
			break
		temp = array[i]
		array[i] = array[j]
		i+=1
		array[j] = temp
		j-=1
	#print "i=", i, ",j=", j, array
	if (i-1 -startIndex >=1): 
		quickSort(array, startIndex, i-1)
	else:
		quickSort(array, startIndex, i)
	if (endIndex - i >=1 ): 
		quickSort(array, i, endIndex)
	else:
		quickSort(array, i-1, endIndex)

print "quickSort test:"
l4 = [15,0,8,8,2,6,10,14,4,12,1,11,9,3,7,5,13]
quickSort(l4, 0, len(l4)-1)
print "array=", l4

def find_kth_element(array, kth, startIndex, endIndex):
	i= startIndex
	j= endIndex
	pivot = array[startIndex+(endIndex-startIndex)/2]
	temp = 0
	if (endIndex-startIndex<=1):
		if (array[startIndex]>array[endIndex]):
			temp = array[startIndex]
			array[startIndex] = array[endIndex]
			array[endIndex] = temp
		return array[kth-1]
	while (i<j):
		while(array[i]<pivot):
			i+=1
		while (array[j]>pivot):
			j-=1
		if (i>=j): break
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		i+=1
		j-=1
	if (i>=kth):
		return find_kth_element(array, kth, 0, j)
	else:
		return find_kth_element(array, kth, i, endIndex)

l5 = [15,0,8,8,2,6,10,14,4,12,1,11,9,3,7,5,13]

for i in range(1,len(l5)+1):
	l6 =list(l5) #make new list
	print i,"\bth element is ",find_kth_element(l6, i, 0, len(l5)-1), l6
