#!/usr/bin/python

def nearest_neighbor(array, item):
	#item=(name, Location_number)
	#array[i] = item
	array = sorted(array, key = lambda x : x[1])	#sort on second element in item
	print array
	i = array.index(item)
	temp = array[i-3:i] + array[i+1:i+4]
#	temp = [ (x,abs(y-item[1])) for x,y in temp ] #works
#	temp = sorted(temp, key = lambda x : x[1])	#here x is the item of the list
#	temp = temp[:3]
#	temp = [ (x,abs(y+item[1])) for (x,y) in temp ]	#works
#	return temp
	temp = sorted(temp, key = lambda x : abs(x[1]-item[1]))	#here x is the item of the list
	temp = temp[:3]
	return temp

#array = [('a', 1),('b', 3),('c', 2), ('d',5),('e',4),('f',7),('g',6),('h',9),('i',8),('j',0)]
#print nearest_neighbor(array, ('h',9))

def every_one_nearest_neighbor(array):
	#item=(name, Location_number)
	#array[i] = item
	nnarray = []
	array = sorted(array, key = lambda x : x[1])	#sort on second element in item
	print array
	for i in range( len(array) ):
		item = array[i]
		temp = array[i-3:i] + array[i+1:i+4]
		temp = sorted(temp, key = lambda x : abs(x[1]-item[1]))	#here x is the item of the list
		temp = temp[:3]
		#nnarray.append( ( item, (temp) ) )
		nnarray.append( ( item, temp ) )	# add a tuple element
	return nnarray

array = [('a', 1),('b', 3),('c', 2), ('d',5),('e',4),('f',7),('g',6),('h',9),('i',8),('j',0)]
#print nearest_neighbor(array, ('h',9))
print every_one_nearest_neighbor(array)
