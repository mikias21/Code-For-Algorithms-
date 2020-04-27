class DynamicCircularQueue(object):
	def __init__(self , limit=5):
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
		return self.queue[self.front]

	def getRear(self):
		if self.rear is None:
			raise Exception("Queue is empty")
		return self.queue[self.rear]

	def enQueue(self,data):
		if self.size == self.limit:
			self.resize()
		self.queue.append(data)
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = self.size 
		self.size += 1
		print("The queue after being enQueue: {}".format(self.queue))

	def deQueue(self):
		if self.size == 0:
			raise Exception("Queue Underflow")
		item = self.queue.pop(0)
		self.size -= 1
		if self.size == 0:
			self.front = self.rear = None 
		else:
			self.rear = self.size - 1
		print("The dequeued item is {}".format(item))
		print("The queue after the dequeue is {}".format(self.queue))

	def resize(self):
		newQueue = list(self.queue)
		self.limit *= 2
		self.queue = newQueue


def main():
	queue = DynamicCircularQueue(3)
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
			item = input("Enter item to inser: ")
			if item is "":
				print("Empty data is not allowed")
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
			print("Incorrect choice")
		choice = input("Do you want to continue? (y/n)")
		if choice == 'y' or choice == 'Y':
			pass
		else:
			flag = False



if __name__ == '__main__':
	main()


