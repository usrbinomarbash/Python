# ── Queue (Linked List implementation) ───────────────────────────────────────


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front  = None
        self.rear   = None
        self._size  = 0

    def enqueue(self, toAdd):
        node = Node(toAdd)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear      = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        data       = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def __repr__(self):
        items, curr = [], self.front
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        return "FRONT -> " + " -> ".join(items) + " <- REAR"


# ── Menu ──────────────────────────────────────────────────────────────────────

def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Enqueue (Add to Rear)")
    print("\n\t\t2. Dequeue (Remove from Front)")
    print("\n\t\t3. Peek Front")
    print("\n\t\t4. Display Queue")
    print("\n\t\t5. Size / Check if Empty")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def main():
    q = Queue()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-6.")
            continue

        if choice == 1:
            print("\n\t\tEnter value to enqueue: ", end="")
            value = input().strip()
            q.enqueue(value)
            print(f"\n\t\t'{value}' enqueued successfully!")

        elif choice == 2:
            try:
                val = q.dequeue()
                print(f"\n\t\t'{val}' dequeued from the front!")
            except IndexError:
                print("\n\t\tQueue is EMPTY! Nothing to dequeue.")

        elif choice == 3:
            try:
                print(f"\n\t\tFront of queue: '{q.peek()}'")
            except IndexError:
                print("\n\t\tQueue is EMPTY!")

        elif choice == 4:
            if q.is_empty():
                print("\n\t\tQueue is EMPTY!")
            else:
                print(f"\n\t\t{q}")

        elif choice == 5:
            print(f"\n\t\tSize   : {q.size()}")
            print(f"\n\t\tEmpty? : {'Yes' if q.is_empty() else 'No'}")

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")


main()