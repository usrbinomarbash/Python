class Queue:
    def __init__(self, size=20):
        self.size = size
        self.data = [None] * self.size
        self.front = -1
        self.rear = -1
        self.count = 0

    def enqueue(self, toAdd):
        if self.count == self.size:
            raise OverflowError("enqueue to full queue")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size   # wrap around
        self.data[self.rear] = toAdd
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        removed = self.data[self.front]
        self.data[self.front] = None
        if self.count == 1:          # queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size  # wrap around
        self.count -= 1
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self.data[self.front]

    def is_empty(self):
        return self.count == 0

    def __repr__(self):
        if self.is_empty():
            return "FRONT -> <- REAR"
        items = []
        for i in range(self.count):
            items.append(str(self.data[(self.front + i) % self.size]))
        return "FRONT -> " + " -> ".join(items) + " <- REAR"


myQue = Queue()
for q in [15, 1, 5, 21, 1, 6, 1, 56, 541, 6, 41, 16, 1, 621]:
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