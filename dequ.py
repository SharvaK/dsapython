class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self,item):
        self.items.append(item)

    def addFront(self,item):
        self.items.insert(0,item)

    def removeFront(self,item):
        self.items.pop(0)

    def removeRear(self,item):
        self.items.pop()

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.addRear(9)
d.addRear(7)
d.addFront(5)
d.addFront(6)
d.addFront(12)
print(d.items)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear(2))
print(d.removeFront(1))
d.addFront(55)
d.addFront(45)
print(d.items)



