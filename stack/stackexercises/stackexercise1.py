class LinkedList(object):
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

	def deleteHead(self):
		if self.head is None or self.length == 0:
			print("Stack Underflow")
		elif self.length == 1:
			data = self.head.getData()
			self.head = None 
			self.length -= 1
			return data 
		else:
			current = self.head 
			self.head = self.head.getNext()
			self.length -= 1
			return current.getData()
			del current

class Stack(object):
	def __init__(self):
		self.stack = LinkedList() 
	def size(self):
		# print(self.stack.getLength())
		return self.stack.getLength()
	def printStack(self):
		self.stack.printList()
	def top(self):
		print(self.stack.getHead())
	def push(self,data):
		self.stack.insertHead(data)
	def pop(self):
		data =  self.stack.deleteHead()
		print("the poped data is {} ".format(data))
		return data 
	def isEmpty(self):
		if self.stack.getLength() == 0:
			return True
		else:
			return False


def matches(open_brc , close_brc):
	matched = False
	if open_brc == '[' and close_brc == ']':
		matched = True
	elif open_brc == '(' and close_brc == ')':
		matched = True
	elif open_brc == '{' and close_brc == '}':
		matched = True
	else:
		pass
	return matched

def balanceBraces(input_val):
	stack = Stack()
	open_br = ['(','[','{']
	close_br = [')',']','}']
	poped_val = None 
	balanced = False

	for i in input_val:
		if i in open_br:
			stack.push(i)
		elif i in close_br:
			if stack.isEmpty() is not True:
				poped_val = stack.pop()
				if matches(poped_val , i):
					balanced = True
				else:
					balanced = False
		else:
			pass
	if balanced:
		print("All braces are balanced")
	else:
		print("Some braces are not balanced")

def infixToPostfix(expression):
	stack = Stack()
	operators = ['%','^','*','-','+','/']
	postfix = ""
	for exp in expression:
		if exp in operators:
			stack.push(exp)
		else:
			postfix += exp
	stackSize = stack.size()
	while stackSize != 0:
		postfix += stack.pop()
		stackSize -= 1
	print("the postfix expression is {}".format(postfix))

expression = "ab-"
infixToPostfix(expression)

####################################
# SOLVE BALANCE BRACES PROBLEM 
# PREFIX , INFIX , POSTFIX problems
