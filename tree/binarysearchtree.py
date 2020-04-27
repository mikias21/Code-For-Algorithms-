# the following code creates a binary tree 

class BinaryTree(object):

	class _Node:

		def __init__(self, value , left = None, right = None):
			self.value = value
			self.left = left 
			self.right = right

		def setValue(self, value):
			self.value = value

		def getValue(self):
			return self.value

		def setLeft(self, left):
			self.left = left 

		def getLeft(self):
			return self.left 

		def setRight(self, right):
			return self.right 

		def  getRight(self):
			return self.right

		def __iter__(self):

			if self.left is not None:
				for element in self.left:
					yield element

			yield self.value

			if self.right is not None:
				for element in self.right:
					yield element 

	def __init__(self):
		self.root = None 

	def insert(self, value):

		def _insert(root, value):

			if root == None:
				return BinaryTree._Node(value)
			elif value < root.getValue():
				root.setLeft(_insert(root.getLeft(), value))
			else: 
				root.setRight(_insert(root.getRight(), value))
			return root

		self.root = _insert(self.root, value)

	def __iter__(self):
		if self.root is not None:
			return self.root.__iter__()
		else:
			return [].__iter__()



def main():
	input_value = input("Enter a list of numbers : ")
	lst = input_value.split()

	tree = BinaryTree()

	for element in lst:
		tree.insert(float(element))

	for x in tree:
		print(x)

if __name__ == '__main__':
	main()

























