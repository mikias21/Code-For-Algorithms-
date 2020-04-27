class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.next = None
        self.prev = None
        self.data = None
        self.length = 0
    #setters and getters
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def setPrev(self,prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def getLength(self):
        return self.length

    #util methods
    def printList(self):
        current = self.head
        while current is not None:
            print("{} -> ".format(current.getData()) , end='')
            current = current.getNext()

    #insertions and deletions , search , reverse , empty
    def insertHead(self,data):
        newNode = DoubleLinkedList()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
            self.head.setNext(None)
            self.head.setPrev(None)
            self.length += 1
        else:
            newNode.setNext(self.head)
            newNode.setPrev(None)
            self.head.setPrev(newNode)
            self.head = newNode
            self.length += 1

    def insertEnd(self,data):
        if self.length == 0:
            newNode = DoubleLinkedList()
            newNode.setData(data)
            self.head = newNode
        else:
            newNode = DoubleLinkedList()
            newNode.setData(data)
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            newNode.setNext(None)
            newNode.setPrev(current)
            current.setNext(newNode)
            self.length += 1

    def insertAtRandomPos(self,pos,data):
        if pos == 0:
            self.insertHead(data)
        elif pos == self.length - 1:
            self.insertEnd(data)
        elif pos < 0 or pos > self.length:
            raise Exception("Invalid position")
        else:
            counter = 1
            current = self.head
            newNode = DoubleLinkedList()
            newNode.setData(data)
            while current.getNext() is not None and counter != pos:
                counter += 1
                current = current.getNext()
            newNode.setNext(current.getNext())
            newNode.setPrev(current)
            current.setNext(newNode)
            self.length += 1

    def deleteHead(self):
        if self.head is None:
            raise Exception('List is Empty')
        else:
            current = self.head
            self.head = self.head.getNext()
            self.head.setPrev(None)
            del current
            self.length -= 1

    def deleteEnd(self):
        if self.head is None:
            raise Exception('List is Empty')
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.getPrev().setNext(None)
            del current
            self.length -= 1

    def deleteAtRandomPos(self,pos):
        if self.head is None:
            raise Exception('List is empty')
        elif pos < 0 or pos > self.length:
            raise Exception('Invalid Position')
        elif pos == 0:
            self.deleteHead()
        elif pos == self.length - 1:
            self.deleteEnd()
        else:
            current = self.head
            counter = 1
            while current.getNext() is not None and counter != pos:
                current = current.getNext()
                counter += 1
            current.getPrev().setNext(current.getNext())
            current.getNext().setPrev(current.getPrev())
            del current
            self.length -= 1

    def searchItem(self,data):
        if self.head is None:
            raise Exception('List is empty')
        elif data == self.head.getData():
            print("Item found on index {}".format(0))
        else:
            counter = 0
            current = self.head
            while current.getNext() is not None and current.getData() != data:
                current = current.getNext()
                counter += 1
            if current.getData() == data:
                print("Item found on index {}".format(counter))
            else:
                print("Item not found")

    def reverseList(self):
        current = self.head
        tmp = None
        while current is not None:
            tmp = current.getPrev()
            current.setPrev(current.getNext())
            current.setNext(tmp)
            current = current.getPrev()

        if tmp is not None:
            self.head = tmp.getPrev()

    def emptyList(self):
        self.head = None

double = DoubleLinkedList()
double.insertHead(1)
double.insertHead(2)
double.insertHead(3)
double.insertEnd(5)
double.insertEnd(6)
double.insertEnd(7)
double.insertEnd(8)
double.insertAtRandomPos(0,21)
double.insertAtRandomPos(5,21)
double.insertAtRandomPos(double.getLength()-1,21)
double.deleteHead()
double.deleteEnd()
double.deleteAtRandomPos(5)
double.searchItem(3)
double.reverseList()
# double.emptyList()
double.printList()
