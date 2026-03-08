class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"N: {self.data} -> ({self.next})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def __repr__(self):
        s = ""
        curr = self.head
        while curr:
            s += f" {curr.data} -> "
            curr = curr.next
        s += " None "
        return s 
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        new_node = Node(data) 
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, target):
        # target is the only node
        if self.head == self.tail:
            if self.head.data == self.tail.data == target:
                self.head = self.tail = None
                return 1
        
        # target is the head
        if self.head.data == target:
            self.head = self.head.next
            return 1
        
        curr = self.head
        while curr:
            if curr.next.data == target:
                # checks if tails is the one to get deleted
                if curr.next.next == None:
                    self.tail = curr
                curr.next = curr.next.next
                return 1
            curr = curr.next
        return -1
        
    def update(self, target, new_data):
        curr = self.head
        while curr:
            if curr.data == target:
                curr.data = new_data
                return 1
            curr = curr.next
        return -1
    
    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

def count(node):
    return 1 + count(node.next) if node else 0

def main():
    new_node = Node(5)
    ll = LinkedList()
    ll.append(6)
    ll.size()
    print(ll.head)


main()
    