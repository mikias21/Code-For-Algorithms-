class LinkedList(object):
    def __init__(self):
        self.head = None
        self.next = None
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
    def getLength(self):
        return self.length
    #util method
    def printList(self):
        current = self.head
        while current is not None:
            print("{} -> ".format(current.getData()) , end='')
            current = current.getNext()

    #main methods insertion and deletion , search , reverse , and empty
    def insertHead(self,data):
        newNode = LinkedList()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
            self.length += 1
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.length += 1

    def insertTail(self,data):
        if self.length == 0:
            self.insertHead(data)
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            newNode = LinkedList()
            newNode.setData(data)
            current.setNext(newNode)
            newNode.setNext(None)
            self.length += 1

    def insertRandomPos(self,pos,data):
        if pos < 0 or pos > self.length:
            raise Exception("Invalid Position !")
        elif pos == 0:
            self.insertHead(data)
        elif pos == self.length - 1:
            self.insertTail(data)
        else:
            counter = 1
            current = self.head
            while counter != pos  and current.getNext() is not None:
                current = current.getNext()
                counter += 1
            newNode = LinkedList()
            newNode.setData(data)
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            self.length += 1

    def deleteHead(self):
        if self.head is None:
            raise Exception("List is empty")
        elif self.length == 1:
            self.head = None
            self.length = 0
        else:
            current = self.head
            self.head = self.head.getNext()
            del current
            self.length -= 1

    def deleteTail(self):
        if self.head is None:
            raise Exception("List is empty")
        elif self.length == 1:
            self.head = None
        else:
            current = self.head
            prev = None
            while current.getNext() is not None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            del current

    def deleteRandomPosition(self,pos):
        if self.head is None:
            raise Exception("List is empty")
        elif self.length == 1:
            self.head = None
            self.length = 0
        elif pos < 0 or pos > self.length:
            raise Exception("Invalid Position !")
        else:
            counter = 1
            current = self.head
            prev = None
            while current.getNext() is not None and counter != pos:
                prev = current
                current = current.getNext()
                counter += 1
            prev.setNext(current.getNext())
            del current
            self.length -= 1

    def searchItem(self,data):
        if self.head is None:
            raise Exception("List is empty")
        else:
            current = self.head
            counter = 0
            while current.getNext() is not None and current.getData() != data:
                current = current.getNext()
                counter += 1
            if current.getData() == data:
                print("Item found on index {}".format(counter))
            else:
                print("Item not found")


    def reverseList(self):
        if self.head is None:
            raise Exception("List is empty")
        else:
            current = self.head
            prev = None
            next = None
            while current is not None:
                next = current.getNext()
                current.setNext(prev)
                prev = current
                current = next
            self.head = prev

    def emptyList(self):
        self.head = None



linkedlist = LinkedList()
linkedlist.insertHead(1)
linkedlist.insertHead(2)
linkedlist.insertHead(3)
linkedlist.insertTail(4)
linkedlist.insertTail(5)
linkedlist.insertTail(6)
linkedlist.insertRandomPos(4,21)
linkedlist.insertRandomPos(0,21)
linkedlist.insertRandomPos(linkedlist.getLength(),21)
linkedlist.deleteHead()
linkedlist.deleteTail()
linkedlist.deleteRandomPosition(4)
linkedlist.searchItem(6)
linkedlist.reverseList()
linkedlist.searchItem(6)
# linkedlist.emptyList()
linkedlist.printList()
