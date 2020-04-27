class LinkedList(object):
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

	def printList(self):
		current = self.head 
		while current is not None:
			print("{} -> ".format(current.getData()) , end='')
			current = current.getNext()

	def insertHead(self,data):
		newNode = LinkedList()
		newNode.setData(data)
		if self.length == 0 or self.head is None:
			self.head = newNode
			self.length += 1
		else:
			newNode.setNext(self.head)
			self.head = newNode
			self.length += 1


	def insertIntoSortedList(self,data):
		newNode = LinkedList()
		newNode.setData(data)
		if self.head is None or self.length == 0:
			self.head = newNode
			self.length += 1
		elif data < self.head.getData():
			newNode.setNext(self.head)
			self.head = newNode
			self.length += 1
		else:
			current = self.head 
			prev = None
			while current.getNext() is not None and current.getData() < data:
				prev = current
				current = current.getNext()
			if current.getNext() is None:
				current.setNext(newNode)
				newNode.setNext(None)
				self.length += 1
			else:
				newNode.setNext(current)
				prev.setNext(newNode)
				self.length += 1

	def reverseList(self):
		if self.head is None:
			raise Exception("List is Empty")
		else:
			current = self.head 
			prev = None 
			next = None 
			while current is not None:
				next = current.getNext()
				current.setNext(prev)
				prev = current
				current = next
			if prev is not None:
				self.head = prev

	def FloydAlogorithm(self):
		slowptr = self.head 
		fastptr = self.head 
		while slowptr and fastptr:
			fastptr = fastptr.getNext()
			if fastptr is slowptr:
				return True 
			if fastptr is None:
				return False 
			fastptr = fastptr.getNext()
			if fastptr is slowptr:
				return True 
			slowptr = slowptr.getNext()
		return False 

# 0 1 2 3 4 5 6 
# 7

linked = LinkedList()
linked.insertHead(6)
linked.insertHead(5)
linked.insertHead(4)
linked.insertHead(3)
linked.insertHead(2)
linked.insertHead(1)
linked.insertHead(0)
linked.insertIntoSortedList(-1)
linked.insertIntoSortedList(7)
linked.insertIntoSortedList(4.5)
linked.reverseList()
linked.printList()
print()
print(linked.getHead())