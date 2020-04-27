class Stack(object):
	#constructor
	def __init__(self):
		self.top = None
		self.next = None
		self.data = None
		self.length  = 0
	#constructor
	def setData(self , data):
		self.data = data 
	def getData(self):
		return self.data 
	def setNext(self , next):
		self.next = next 
	def getNext(self):
		return self.next 
	def getLength(self):
		return self.length 
	#util methods
	def printList(self):
		current = self.head
		while current is not None:
			print("{} -> ".format(current.getData()) , end='')
			current = current.getNext()

	#main methods insert at the top and delete at the top
	def insertHead(self , data):
		newNode = Stack()
		newNode.setData(data)
		if self.length == 0:
			self.head = newNode
			self.length += 1
		else:
			newNode.setNext(self.head)
			self.head = newNode
			self.length += 1

	def deleteHead(self):
		if self.head == None or self.length == 0:
			raise Exception("List is empty")
		else:
			current = self.head 
			self.head = self.head.getNext()
			self.length -= 1
			del current


stack = Stack()
stack.insertHead(1)
stack.insertHead(2)
stack.insertHead(3)
stack.deleteHead()
stack.deleteHead()
stack.insertHead(19)
stack.insertHead(21)
stack.insertHead(27)
stack.printList()