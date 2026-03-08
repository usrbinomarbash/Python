class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, toAdd):
        node = Node(toAdd)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def __repr__(self):
        items, curr = [], self.front
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        return "FRONT -> " + " -> ".join(items) + " <- REAR"
    
myQue = Queue()
for q in [15,1,5,21,1,6,1,56,541,6,41,16,1,621]:
    myQue.enqueue(q)
print(myQue)
print(myQue.peek())
print(myQue.dequeue())
print(myQue.dequeue())
print(myQue)
print(myQue.is_empty())
myQue.dequeue()
myQue.dequeue()
myQue.dequeue()
myQue.dequeue()
myQue.dequeue()

print(myQue.is_empty())
print(myQue)
