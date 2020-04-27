class LinkedListQueue(object):
	def __init__(self):
		self.head = None
		self.next = None
		self.data = None
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

	def getTail(self):
		current = self.head 
		while current.getNext() is not None:
			current = current.getNext()
		return current.getData()

	def printList(self):
		current = self.head 
		while current is not None:
			print("{} -> ".format(current.getData()) , end="")
			current = current.getNext()
		print()

	def insertEnd(self,data):
		newNode = LinkedListQueue()
		newNode.setData(data)
		if self.length == 0:
			self.head = newNode
			self.head.setNext(None)
			self.length += 1
		else:
			current = self.head
			while current.getNext() is not None:
				current = current.getNext()
			current.setNext(newNode)
			newNode.setNext(None)
			self.length += 1

	def deleteHead(self):
		if self.length == 0:
			raise Exception("List is empty")
		elif self.length == 1:
			self.head = None
			self.length = 0 
		else:
			current = self.head
			item = current.getData() 
			self.head = self.head.getNext()
			del current
			self.length -= 1
		print("the dequeued item is {}".format(item))

class Queue(object):
	def __init__(self):
		self.linkedlist = LinkedListQueue()

	def getSize(self):
		return self.linkedlist.getLength()

	def getFront(self):
		return self.linkedlist.getHead()

	def getRear(self):
		return self.linkedlist.getTail()

	def enQueue(self,data):
		self.linkedlist.insertEnd(data)
		self.linkedlist.printList()

	def deQueue(self):
		self.linkedlist.deleteHead()
		self.linkedlist.printList()



def main():
	queue = Queue()
	flag = True
	while flag:
		print("1. Enqueue")
		print("2. Dequeue")
		print("3. Get Front")
		print("4. Get Rear")
		print("5. Get Size")
		print("6. Exit")
		ch = int(input(""))
		if ch == 1:
			item = input("Enter item to the queue: ")
			if item is "":
				print("empty item is not allowed")
				return 
			else:
				queue.enQueue(item)
		elif ch == 2:
			queue.deQueue()
		elif ch == 3:
			print(queue.getFront())
		elif ch == 4:
			print(queue.getRear())
		elif ch == 5:
			print(queue.getSize())
		elif ch == 6:
			exit()
		else:
			print("Incorrect Choice")
		choice = input("Do you want to continue(y/n)? ")
		if choice == 'y' or choice == 'Y':
			pass
		else:
			flag = False

if __name__ == '__main__':
	main()




	
