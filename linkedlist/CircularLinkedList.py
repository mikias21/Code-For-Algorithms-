#Circular linked list class
class CircularLinkedList(object):
	#constructor
	def __init__(self):
		self.head = None
		self.data = None 
		self.next = None
		self.length = 0

	#setters and getters
	def setData(self, data):
		self.data = data 
	def getData(self):
		return self.data 
	def setNext(self, next):
		self.next = next 
	def getNext(self):
		return self.next 
	def getLength(self):
		return self.length 

	#util methods
	def printList(self):
		current = self.head
		if current is None:return 0
		print("{} -> ".format(current.getData()) , end='')
		while current.getNext() is not self.head and current.getNext() is not None:
			current = current.getNext()
			print("{} -> ".format(current.getData()) , end='')

	#main functions insert , delete , search , reverse
	def insertHead(self, data):
		newNode = CircularLinkedList()
		newNode.setData(data)
		newNode.setNext(newNode)
		if self.length == 0:
			self.head = newNode
			self.length += 1
		else:
			current = self.head 
			while current.getNext() is not self.head:
				current = current.getNext()
			newNode.setNext(self.head)
			current.setNext(newNode)
			self.head = newNode
			self.length += 1

	def insertEnd(self, data):
		newNode = CircularLinkedList()
		newNode.setData(data)
		if self.length == 0:
			newNode.setNext(newNode)
			self.head = newNode
			self.length += 1
		else:
			current = self.head 
			while current.getNext() is not self.head:
				current = current.getNext()
			newNode.setNext(self.head)
			current.setNext(newNode)
			self.length += 1

	def insertAtRandomPos(self,pos,data):
		if pos < 0 or pos > self.length:
			raise Exception("Invalid Position")
		elif pos == 0:
			self.insertHead(data) 
		elif pos == self.length - 1:
			self.insertEnd(data)
		else:
			newNode = CircularLinkedList()
			newNode.setData(data)
			counter = 1
			current = self.head 
			while current.getNext() is not self.head and counter != pos:
				current = current.getNext()
				counter += 1
			newNode.setNext(current.getNext())
			current.setNext(newNode)
			self.length += 1

	def deleteHead(self):
		if self.head is None:
			raise Exception('List is Empty')
		elif self.length == 1:
			self.length = 0
			del self.head
		else:
			current = self.head
			self.head = current.getNext()
			self.length -= 1
			del current

	def deleteEnd(self):
		if self.head is None:
			raise Exception("List is empty")
		elif self.length == 1:
			self.length = 0
			del self.head 
		else:
			current = self.head
			prev = None
			while current.getNext() is not self.head:
				prev = current
				current = current.getNext()
			prev.setNext(self.head)
			self.length -= 1
			del current

	def deleteAtRandomPos(self,pos):
		if pos < 0 or pos > self.length:
			raise Exception("Invalid Position")
		elif pos == 0:
			self.deleteHead()
		elif pos == self.length - 1:
			self.deleteEnd()
		else:
			current = self.head
			prev = None 
			counter = 1
			while current.getNext() is not self.head and counter != pos:
				prev = current
				current = current.getNext()
				counter += 1
			prev.setNext(current.getNext())
			self.length -= 1
			del current

	def searchList(self,data):
		indices = []
		if self.head is None:
			raise Exception("List is empty")
		else:
			counter = 0
			current = self.head
			if current.getData() is data: indices.append(counter)
			while current.getNext() is not self.head:
				counter += 1
				if current.getData() is data:
					indices.append(counter)
				current = current.getNext()
		return indices


	def reverseList(self):
		if self.head is None:
			raise Exception("List is empty")
		else:
			current = self.head
			prev = None 
			next = None 
			while current.getNext() is not self.head:
				next = current.getNext()
				current.setNext(prev)
				prev = current
				current = next
			if prev is not None:self.head = prev 


	def emptyList(self):
		self.head = None

cirlinkedlist = CircularLinkedList()
cirlinkedlist.insertHead(1)
cirlinkedlist.insertHead(2)
cirlinkedlist.insertHead(3)
cirlinkedlist.insertHead(9)
cirlinkedlist.insertEnd(4)
cirlinkedlist.insertEnd(5)
cirlinkedlist.insertEnd(6)
cirlinkedlist.insertAtRandomPos(0,21)
cirlinkedlist.insertAtRandomPos(cirlinkedlist.getLength() - 1,21)
cirlinkedlist.insertAtRandomPos(5,21)
cirlinkedlist.deleteHead()
cirlinkedlist.deleteEnd()
cirlinkedlist.insertHead(21)
cirlinkedlist.deleteAtRandomPos(5)
cirlinkedlist.printList()
print()
print(cirlinkedlist.searchList(21))
cirlinkedlist.reverseList()
# cirlinkedlist.emptyList()
cirlinkedlist.printList()
