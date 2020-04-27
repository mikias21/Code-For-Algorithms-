from queueExercise import CircularQueueDynamic


class Stack(object):
	def __init__(self):
		self.head = None 
		self.data = None
		self.next = None
		self.size = 0 

	def setData(self,data):
		self.data = data 
	def getData(self):
		return self.data 
	def setNext(self,next):
		self.next = next
	def getNext(self):
		return self.next
	def getSize(self):
		return self.size 

	def print(self):
		current = self.head 
		while current is not None:
			print("{} ".format(current.getData()) ,end='')
			current = current.getNext()
		print()

	def push(self,data):
		newNode = Stack()
		newNode.setData(data)
		if self.head == None:
			self.head = newNode
			self.size += 1
		else:
			newNode.setNext(self.head)
			self.head = newNode
			self.size += 1

	def pop(self):
		if self.head is None:
			raise Exception("List is empty")
		elif self.size == 1:
			item = self.head.getData()
			self.head = None
			self.size = 0
			return item
		else:
			current = self.head
			item = self.head.getData()
			self.head = self.head.getNext()
			self.size -= 1
			del current 
			return item



def reverseCircularQueue():
	cirqueue = CircularQueue()
	stack = Stack()
	cirqueue.enQueue('a')
	cirqueue.enQueue('b')
	cirqueue.enQueue('c')
	cirqueue.enQueue('d')
	print()
	print()
	print("Reversing ........")
	print()
	print()
	queuesize = cirqueue.getSize()
	while queuesize > 0:
		stack.push(cirqueue.deQueue())
		queuesize -= 1
	stacksize = stack.getSize()
	print()
	print()
	while stacksize > 0:
		cirqueue.enQueue(stack.pop())
		stacksize -= 1


def checkIfConsecutiveNums():
	cirqueue = CircularQueueDynamic()
	cirqueue.enQueue(4)
	cirqueue.enQueue(5)
	cirqueue.enQueue(-2)
	cirqueue.enQueue(-3)
	cirqueue.enQueue(11)
	cirqueue.enQueue(10)
	cirqueue.enQueue(5)
	cirqueue.enQueue(6)
	cirqueue.enQueue(20)

	counter = 0
	# print(cirqueue.getSize())
	if cirqueue.getSize() % 2 != 0:
		while counter < cirqueue.getSize() - 1:
			item = cirqueue.deQueue()
			print(cirqueue.getFront())
			counter += 1
	else:
		print("even")

checkIfConsecutiveNums()

# reverseCircularQueue()