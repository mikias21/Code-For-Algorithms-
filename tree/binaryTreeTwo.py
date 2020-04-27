class Tree:

	def __init__(self, data):
		self.data = data 
		self.left = None 
		self.rigt = None 


	def insert(self, data):
		if self.data is not None:
			if self.data < data:
				if self.left is None:
					self.left = Tree(data)
				else:
					self.left.insert(data)
			else:
				if self.rigt is None:
					self.rigt = Tree(data)
				else:
					self.rigt.insert(data)
		else:
			self.data = data 

	def printTree(self):
		if self.left is not None:
			self.left.printTree()
		print(str(self.data) + " ", end='')
		if self.rigt is not None:
			self.rigt.printTree()


tree = Tree(0)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.printTree()

