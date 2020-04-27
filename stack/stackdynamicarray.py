class Stack(object):
	def __init__(self,limit=10):
		self.limit = limit
		self.stack = self.limit * [None]

	def size(self):
		return len(self.stack)

	def printStack(self):
		print(self.stack)

	def top(self):
		if self.size() == 0:
			print("Stack underflow")
		else:
			return self.stack[:-1]

	def resize(self):
		newStack = list(self.stack)
		self.limit *= 2
		self.stack = newStack 

	def push(self,data):
		if self.size() >= self.limit:
			self.resize()
		self.stack.append(data)

	def pop(self):
		if self.size() == 0:
			print("Stack underflow")
		else:
			print("the poped item is {} ".format(self.stack.pop()))


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.printStack()
