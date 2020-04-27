class Queue(object):
	def __init__(self,limit=5):
		self.queue = []
		self.front = None
		self.rear = None 
		self.size = 0
		self.limit = limit 

	def getSize(self):
		return self.size 

	def getFront(self):
		if self.front is None:
			raise Exception("Queue is empty")
			return
		return self.queue[self.front]

	def getRear(self):
		if self.rear is None:
			raise Exception("Queue is empty")
			return 
		return self.queue[self.rear]

	def enQueue(self,data):
		if self.size == self.limit:
			raise Exception("Queue Overflow")
			return 
		else:
			self.queue.append(data)
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = self.size 
		self.size += 1
		print("Queue after being enqueued is : {}".format(self.queue))

	def deQueue(self):
		if self.size <= 0:
			raise Exception("Queue Underflow")
			return 
		else:
			item = self.queue.pop(0)
			self.size -= 1
			if self.size == 0:
				self.front = self.rear = None 
			else:
				self.rear = self.size - 1
		print("the dequeued item is {}".format(item))
		print("Queue after being dequeued is : {}".format(self.queue))


def main():
	queue = Queue()
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