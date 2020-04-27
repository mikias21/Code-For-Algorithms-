# traversing ASTs (Abstract Syntax Tress)

class TimesNode(object):

	def __init__(self, left, right):
		self.right = right 
		self.left = left 

	def eval(self):
		return self.left.eval() * self.right.eval()

	def inOrder(self):
		return "({} * {})".format(self.left.inOrder() , self.right.inOrder())

class PlusNode(object):

	def __init__(self, left, right):
		self.right = right 
		self.left = left 

	def eval(self):
		return self.left.eval() + self.right.eval()

	def inOrder(self):
		return "({} + {})".format(self.left.inOrder() , self.right.inOrder())

class NumNode(object):

	def __init__(self, num):
		self.num = num 

	def eval(self):
		return self.num

	def inOrder(self):
		return str(num)

def main():
	num1 = NumNode(5)
	num2 = NumNode(4)
	plus = PlusNode(num1 , num2)
	times = TimesNode(plus , NumNode(6))
	root = PlusNode(times , NumNode(3))
	print(root.eval())

if __name__ == '__main__':
	main()