class Node:
	""" a node definition used in a tree or list """
#	#root = None			# class variable shared by all instances
	def __init__(self, data):
		self.data = data	# instance variable unique to each instance
		self.left = None
		self.right = None
	def __str__(self):	#same as java toString() method
		if (self.left==None):
			sleft="its left is None"
		else:
			sleft="its left is "+str(self.left.data)
		if (self.right==None):
			sright="its right is None"
		else:
			sright="its right is "+str(self.right.data)
		return "Node.data="+str(self.data)+", "+sleft+", "+sright
class BinaryTree:
	""" a binary tree definition """
	def __init__(self):
		self.root = None
	def __str__(self):
		return self.tostring(self.root)
	def tostring(self, node):
		if node==None:
			return ""
		if node.left!=None:
			sTree=self.tostring(node.left)
			sTree = sTree+","+str(node.data)
		else:
			sTree = str(node.data)
		if node.right!=None:
			sTree= sTree+","+self.tostring(node.right)
		else:
			pass
		return sTree

	def lookup(self, data):
		return self.lookupHelp(self.root, data)
	def lookupHelp(self, node, data):
		if (node==None):
			return False
		if node.data == data:
			return True
		return self.lookupHelp(node.left, data) or self.lookupHelp(node.right, data)
	def insert(self, data):
		self.root = self.insertHelp(self.root, data)
	def insertHelp(self, node, data):
#		print node
		if node==None:
#			print "insertHelp 1"
			return Node(data)
		if data<=node.data:
#			print "insertHelp 2"
			node.left = self.insertHelp(node.left, data)
#			print "insertHelp 2: "+str(node)
		else:
#			print "insertHelp 3"
			node.right = self.insertHelp(node.right, data)
#			print "insertHelp 3: "+str(node)
#		print "insertHelp 4"
#		print "insertHelp 4: "+str(node)
		return node

	def build123(self):
		self.insert(2)
		self.insert(1)
		self.insert(3)
	def addNodeFromArray(self, array=[]):
		for i in range(len(array)):
			self.insert(array[i])
	def size(self):
		return self.sizeHelp(self.root)
	def sizeHelp(self, node):
		if node==None:
			return 0
		return 1 + self.sizeHelp(node.left) + self.sizeHelp(node.right)
	def maxDepth(self):
		return self.maxDepthHelp(self.root)
	def maxDepthHelp(self, node):
		if node==None:
			return 0
		ldepth = self.maxDepthHelp(node.left)
		rdepth = self.maxDepthHelp(node.right)
		if (ldepth>=rdepth):
			return ldepth+1
		else:
			return rdepth+1
	def minValue(self):
		return self.minValueHelp(self.root)
	def minValueHelp(self, node):
		if node==None:
			return None
		while(node.left!=None):
			node = node.left
		return node.data
	def maxValue(self):
		return self.maxValueHelp(self.root)
	def maxValueHelp(self, node):
		if node==None:
			return None
		while(node.right!=None):
			node = node.right
		return node.data
	def printTree(self):
		self.printTreeHelp(self.root)
		print "\b\b "
	def printTreeHelp(self, node):
		if node==None: return
		self.printTreeHelp(node.left)
		print str(node.data)+",",
		self.printTreeHelp(node.right)
	def printPostorder(self):
		self.printPostorderHelp(self.root)
		print "\b\b "
	def printPostorderHelp(self, node):
		if node==None: return
		self.printPostorderHelp(node.left)
		self.printPostorderHelp(node.right)
		print str(node.data)+",",
	def hasPathSum(self, sum):
		return self.hasPathSumHelp(self.root, sum)
	def hasPathSumHelp(self, node, sum):
		if node==None:
			if sum==0:
				return True
			else:
				return False
		sum = sum-node.data
		return self.hasPathSumHelp(node.left, sum) or self.hasPathSumHelp(node.right, sum)
	def printPaths(self):
		if self.root == None: return
		array=[]
		self.printPathsHelp(self.root, array)
	def printPathsHelp(self, node, array=[]):
		array.append(node.data)
		if node.left==None and node.right==None:
			self.printArray(array)
		if node.left!=None:
			l =len(array)
			self.printPathsHelp(node.left, array)
			while(l<len(array)):
				array.pop(),
		if node.right!=None:
			#l=len(array)
			self.printPathsHelp(node.right, array)
			#while(l<len(array)):
			#	array.pop(),
	def printArray(self, array=[]):
		for i in array:
			print i,
		print
	def mirror(self):
		self.mirrorHelp(self.root)
	def mirrorHelp(self, node):
		if node==None: return
		self.mirrorHelp(node.left)
		self.mirrorHelp(node.right)
		temp = node.left
		node.left = node.right
		node.right = temp
	def doubleTree(self):
		self.doubleTreeHelp(self.root)
	def doubleTreeHelp(self, node):
		if node==None:
			return
		self.doubleTreeHelp(node.left)
		self.doubleTreeHelp(node.right)
		temp = Node(node.data)
		temp.left=node.left
		node.left=temp
	def clear(self):
		self.root = None
	def sameTree(self, tree):
		return self.sameTreeHelp(self.root, tree.root)
	def sameTreeHelp(self, a, b):
		if (a==None and b==None):
			return True
		if a.data != b.data:
			return False
		return (self.sameTreeHelp(a.left, b.left) and self.sameTreeHelp(a.right, b.right))
	def countTrees(self, keys):
		if keys<=1: return 1
		sum = 0
		for i in range(1,keys+1):
			lsum = self.countTrees(i-1)
			rsum = self.countTrees(keys-i)
			sum += lsum*rsum
		return sum
	def isBST(self):
		#return self.isBSTHelp1(self.root)
		import sys	# import only in this function
		return self.isBSTHelp2(self.root, -sys.maxint - 1, sys.maxint)
	def isBSTHelp1(self, node):	#works
		if node == None: return True
		if node.left==None and node.right==None:
			return True
		if node.left!=None:
			if node.data < node.left.data:
				return False
		if node.right!=None:
			if node.data >= node.right.data:
				return False
		return self.isBSTHelp1(node.left) and self.isBSTHelp1(node.right)
	def isBSTHelp2(self, node, min, max):
		if node==None: return True
		if node.data < min or node.data > max:
			return False
		return self.isBSTHelp2(node.left, min, node.data) and self.isBSTHelp2(node.right, node.data+1, max)
	def treeToList(self):
		self.root = self.treeToListHelp(self.root)
	def join(self, nodea, nodeb):	# treat the tree node as a double linked list node
		nodea.right=nodeb	#right=next in list
		nodeb.left=nodea	#left=previous in list
	def append(self, lista, listb):
		if lista==None: return listb
		if listb==None: return lista
		alast=lista.left
		blast=listb.left
		self.join(alast, listb)
		self.join(blast, lista)
		return lista
	def treeToListHelp(self, node):
		if node==None: return None
		left=self.treeToListHelp(node.left)
		right=self.treeToListHelp(node.right)
		node.left=node	#make a single node list
		node.right=node
		#print str(node.data)
		left= self.append(left, node)
		left= self.append(left, right)
		#print str(left.data)
		return left
	def printList(self):
		if self.root!=None:
			self.printListHelp(self.root)
	def printListHelp(self, node):
		head = node
		while(True):
			print str(node.data)+",",
			node=node.right
			if node==head: break	#because no do-while in Python
		print "\b\b "

t123 = BinaryTree()
t123.build123()
at123 = BinaryTree()
at123.build123()
print "Two tree are same? "+str(t123.sameTree(at123))

print "The root node is: "+ str(t123.root)
print "The tree size is: "+str(t123.size())
print "Is 6 is in the tree? "+str(t123.lookup(6))
print "The tree max depth is: "+str(t123.maxDepth())
print "The min value in the tree is: "+str(t123.minValue())
print "The max value in the tree is: "+str(t123.maxValue())
print "The tree is:"
t123.printTree()
print "The tree postorder is:"
t123.printPostorder()
print "Is the tree of the path sum of 3: "+str(t123.hasPathSum(3))
print "Is the tree of the path sum of 5: "+str(t123.hasPathSum(5))
print "Is the tree of the path sum of 4: "+str(t123.hasPathSum(4))
print t123
print "The tree paths are:"
t123.printPaths()
print "Mirror the tree:"
t123.mirror()
print t123
print "Two tree are same? "+str(t123.sameTree(at123))
print "Mirror the tree again:"
t123.mirror()
print t123
t123.doubleTree()
print t123
print "clear the tree, and build123 again:"
t123.clear()
t123.build123()
print t123
print "Is the binary search tree? "+ str(t123.isBST())
a=[6,4,7,5,0]
print "The array is: "+ str(a) + " and be added into the tree:"
t123.addNodeFromArray(a)
print t123
print "Is the binary search tree? "+ str(t123.isBST())

print "The root node is: "+ str(t123.root)
print "The tree size is: "+str(t123.size())
print "Is 6 is in the tree? "+str(t123.lookup(6))
print "The tree max depth is: "+str(t123.maxDepth())
print "The min value in the tree is: "+str(t123.minValue())
print "The max value in the tree is: "+str(t123.maxValue())
print "The tree is:"
t123.printTree()
print "The tree postorder is:"
t123.printPostorder()
print "Is the tree of the path sum of 3: "+str(t123.hasPathSum(3))
print "Is the tree of the path sum of 5: "+str(t123.hasPathSum(5))
print "Is the tree of the path sum of 4: "+str(t123.hasPathSum(4))
print t123
print "The tree paths are:"
t123.printPaths()
print "Mirror the tree:"
t123.mirror()
print t123
print "Is the binary search tree? "+ str(t123.isBST())
print "Mirror the tree again:"
t123.mirror()
print t123
print "double the tree:"
t123.doubleTree()
print t123
print "Is the binary search tree? "+ str(t123.isBST())
print "How many BSTs can 4 keys build up?  "+str(t123.countTrees(4))
t123.treeToList()
t123.printList()