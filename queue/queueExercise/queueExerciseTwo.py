import math

class Queue(object):
	def __init__(self , limit = 9):
		self.queue = []
		self.front = None
		self.rear = None
		self.limit = limit
		self.size = 0;

	def getFront(self):
		if self.front is None:
			return None
		else:
			return self.queue[self.front]

	def getRear(self):
		if self.rear is None:
			return None
		else:
			return self.queue[self.rear]

	def getSize(self):
		return self.size 

	def enQueue(self , data):
		if self.size == self.limit:
			self.resize()
		self.queue.append(data)
		if self.front == None:
			self.front = self.rear = 0
		else:
			self.rear = self.size + 1
		self.size += 1
		return self.queue 

	def deQueue(self):
		if self.front is None:
			return 0
		item = self.queue.pop(0)
		self.size -= 1
		if self.size == 0:
			self.front = self.rear = None
		else:
			self.rear = self.size - 1
		return item

	def resize(self):
		newQueue = self.queue 
		self.limit *= 2
		self.queue = list(newQueue)

	def getQueue(self):
		return self.queue

#numbers to work with 4 5 -2 -3 11 10 5 6 20
queue = Queue()
queue.enQueue(4)
queue.enQueue(5)
queue.enQueue(-2)
queue.enQueue(-3)
queue.enQueue(11)
queue.enQueue(10)
queue.enQueue(5)
queue.enQueue(6)
queue.enQueue(20)
nums = queue.getQueue()
# print(nums)

def checkConsecutive():
	nums = [4,5,-2,-3,11,10,5,6,20,21,22,23]
	queue = Queue()
	consecutive = False
	for i in nums:
		queue.enQueue(i)
	counter = 0

	if queue.getSize() % 2 == 0:
		while counter != queue.getSize():
			try:
				x1 = queue.deQueue()
				x2 = queue.deQueue()
				if x1 + 1 == x2 or x1 - 1 == x2 or x2 + 1 == x1 or x2 - 1 == x1:
					consecutive = True
				else:
					consecutive = False
					break
			except Exception:
				pass
			counter += 1
	else:
		while counter != queue.getSize() - 1:
			try:
				x1 = queue.deQueue()
				x2 = queue.deQueue()
				if x1 + 1 == x2 or x1 - 1 == x2 or x2 + 1 == x1 or x2 - 1 == x1:
					consecutive = True
				else:
					consecutive = False
					break
			except Exception:
				pass
			counter += 1


	if consecutive:
		print("Queue items are consecutive")
	else:
		print("Queue items are not consecutive")




def mergeHalfQueue():
	nums = [11,12,13,14,15,16,17,18,19,20]
	merged = []
	firsthalf = []
	counter = 1
	queue = Queue()
	# insert into queue
	for i in nums:
		queue.enQueue(i)
	#start the merge
	for i in range((queue.getSize() // 2)):
		firsthalf.append(queue.deQueue())	
	
	for i in range(len(firsthalf)):
		merged.append(firsthalf[i])
		merged.append(queue.deQueue())
	del firsthalf
	del nums

	print(merged)


def reverseKItemsFromQueue(k):
	nums = [11,12,13,14,15,16,17,18,19,20]
	queue = Queue()
	reverse_ls = []
	new_lst = []
	counter = 0
	# insert into queue
	for i in nums:
		queue.enQueue(i)	
	while counter < k:
		reverse_ls.append(queue.deQueue())
		counter += 1
	for i in reversed(reverse_ls):
		new_lst.append(i)
	for i in range(queue.getSize()):
		new_lst.append(queue.deQueue())

	print(new_lst)


reverseKItemsFromQueue(2)



