class CircularQueue(object):
	def __init__(self , limit=5):
		self.queue = []
		self.front = None
		self.rear = None
		self.size = 0
		self.limit = limit

	def getFront(self):
		if self.front is None:
			raise Exception("Queue is empty")
		return self.queue[self.front] 
	def getRear(self):
		if self.rear is None:
			raise Exception("Queue is empty")
		return self.queue[self.rear] 

	def getSize(self):
		return self.size 

	def enQueue(self,data):
		if self.size == self.limit:
			raise Exception("Queue overflow")
		self.queue.append(data)
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = self.size
		self.size += 1
		print("Queue after being inserted : {}".format(self.queue))

	def deQueue(self):
		if self.size == 0:
			raise Exception("Queue Underflow")
		item = self.queue.pop(0)
		self.size -= 1
		if self.size is None:
			self.front = self.rear = None 
		else:
			self.rear = self.size - 1
		print("The dequeued item is {}".format(item))
		print("The queue after being dequeued {}".format(self.queue))
		return item



class CircularQueueDynamic(object):
	def __init__(self, limit=5):
		self.queue = []
		self.front = None 
		self.rear = None
		self.size = 0
		self.limit = limit

	def getFront(self):
		if self.front is None:
			raise Exception("Queue is Empty")
		return self.queue[self.front]
	def getRear(self):
		if self.rear is None:
			raise Exception("Queue is Empty")
		return self.queue[self.rear]

	def getSize(self):
		return self.size 

	def enQueue(self , data):
		if self.size == self.limit:
			self.resize()
		self.queue.append(data)
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = self.size 
		self.size += 1
		print("the queue after being enqueued: {}".format(self.queue))

	def deQueue(self):
		if self.size == 0:
			raise Exception("Queue Underflow")
		else:
			item = self.queue.pop(0)
			self.size -= 1
			if self.size == 0:
				self.front = self.rear = None 
			else:
				self.rear = self.size - 1
		print("The dequeued item is {}".format(item))
		print("the queue after dequeue: {}".format(item))
		return item

	def resize(self):
		newQueue = self.queue
		self.limit *= 2
		self.queue = newQueue


class LinkedListQueue(object):
	def __init__(self):
		self.head = None 
		self.next = None
		self.data = None
		self.size = 0

	def setNext(self,next):
		self.next = next 
	def getNext(self):
		return self.next 
	def setData(self,data):
		self.data = data 
	def getData(self):
		return self.data 
	def getSize(self):
		return self.size 

	def printList(self):
		current = self.head 
		while current is not None:
			print("{} -> ".format(current.getData()) , end="")
			current = current.getNext()
		print()

	def InsertHead(self,data):
		newNode = LinkedListQueue()
		newNode.setData(data)
		if self.head is None:
			self.head = newNode 
			self.size += 1
		else:
			current = self.head 
			while current.getNext() is not None:
				current = current.getNext()
			current.setNext(newNode)
			newNode.setNext(None)
			self.size += 1

	def DeleteHead(self):
		if self.size == 0:
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
			self.size = 0
			del current
			return item


def main():
	queue = CircularQueue()
	flag = True
	while flag:
		print("1. Enqueue")
		print("2. Dequeue")
		print("3. Front")
		print("4. Rear")
		print("5. Size")
		print("6. Exit")
		choice = int(input("Enter your choice 1 - 6: "))
		if choice == 1:
			print("Enter data to insert: ")
			data = input("")
			if data is None or data == '':
				print("Empty data is not allowed")
				return
			else:
				queue.enQueue(data)
		elif choice == 2:
			queue.deQueue()
		elif choice == 3:
			print(queue.getFront())
		elif choice == 4:
			print(queue.getRear())
		elif choice == 5:
			print(queue.getSize())
		elif choice == 6:
			exit()
		else:
			print("Incorrect choice")
			return 
		print("Do you want to continue(y/n)")
		ch = input("")
		if ch == 'y' or ch == 'Y':
			pass
		else: 
			flag = False


if __name__ == '__main__':
	main()
