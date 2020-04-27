#ASTs stands for Abstract Syntax Tress and Expressions

# The code below will solve (5 + 4) * 6 + 3 in ASTs goes like ((5 + 4) * 6) + 3 = 57

class TimesNode(object):

	def __init__(self, left, right):
		self.left = left
		self.right = right 

	def eval(self):
		return self.left.eval() * self.right.eval()

class PlusNode(object):

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self):
		return self.left.eval() + self.right.eval()

class NumNode(object):

	def __init__(self, num):
		self.num = num 

	def eval(self):
		return self.num 

def main():
	num1 = NumNode(5)
	num2 = NumNode(4)
	plus = PlusNode(num1 , num2)
	times = TimesNode(plus , NumNode(6))
	root = PlusNode(times , NumNode(3))
	print(root.eval())

if __name__ == '__main__':
	main()