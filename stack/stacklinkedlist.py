class Node(object):
	def __init__(self):
		self.head = None
		self.data = None
		self.next = None
		self.length = 0
	def setData(self,data):
		self.data = data
	def getData(self):
		return self.data 
	def setNext(self,next):
		self.next = next 
	def getNext(self):
		return self.next 
	def getLength(self):
		return self.length
	def getHead(self):
		return self.head.getData()

	def printNode(self):
		current = self.head
		print("[ " , end='')
		while current is not None:
			print("{} , ".format(current.getData()) , end='')
			current = current.getNext()
		print(" ]" , end='')

	def insertHead(self,data):
		newNode = Node()
		newNode.setData(data)
		if self.head is None:
			self.head = newNode
			self.length += 1
		else:
			newNode.setNext(self.head)
			self.head = newNode
			self.length += 1

	def deleteHead(self):
		if self.head is None:
			raise Exception("List is empty")
		else:
			current = self.head
			self.head = self.head.getNext()
			self.length -= 1
			print("the poped data is {} ".format(current.getData()))
			del current

class Stack(object):
	def __init__(self):
		self.newNode = Node() 

	def push(self,data):
		self.newNode.insertHead(data)

	def pop(self):
		self.newNode.deleteHead()

	def top(self):
		print(self.newNode.getHead())

	def size(self):
		print(self.newNode.getLength())

	def printStack(self):
		self.newNode.printNode()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.pop()
stack.size()
stack.printStack()

