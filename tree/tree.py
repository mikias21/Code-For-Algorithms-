class Tree(object):
	def __init__(self):
		self.root = None
		self.data = None
		self.left = None 
		self.right = None 

	def setData(self, data):
		self.data = data 
	def getData(self):
		return self.data 
	def getLeft(self):
		return self.left 
	def getRight(self):
		return self.right 
	# type of iterations 
	# preorder DLR
	# inorder LDR
	# postorder LRD

	def preOrderRecursive(self, root, result): 
		if not root:
			return 
		result.append(root.getData())
		preOrderRecursive(root.getLeft(), result)
		preOrderRecursive(root.getRight(), result)

	def inOrderRecursive(self, root, result):
		if not root:
			return
		inOrderRecursive(root.getLeft(), result)
		result.append(root.getData())
		inOrderRecursive(root.getRight(), result)

	def postOrderRecursive(self, root, result):
		if not root:
			return
		postOrderRecursive(root.getLeft(), result)
		postOrderRecursive(root.getRight(), result)
		result.append(root.getData())