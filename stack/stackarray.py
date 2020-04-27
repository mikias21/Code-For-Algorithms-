class Stack(object):
	def __init__(self,limit=10):
		self.limit = limit
		self.stack = []

	def size(self):
		return len(self.stack)
	def push(self,data):
		if self.size() >= self.limit:
			print("stack overflow")
		else:
			self.stack.append(data)
	def pop(self):
		if self.size() == 0:
			print("Stack underflow")
		else:
			print("the poped data is {} ".format(self.stack.pop()))

	def top(self):
		if self.size() == 0:
			print("stack underflow")
		else:
			return self.stack[:-1]

	def printStack(self):
		print(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.printStack()
