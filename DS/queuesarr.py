


class Queue:
    def __init__(self, size=20):
        self.size  = size
        self.data  = [None] * self.size
        self.front = -1
        self.rear  = -1
        self.count = 0

    def enqueue(self, toAdd):
        if self.count == self.size:
            raise OverflowError("enqueue to full queue")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = toAdd
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        removed = self.data[self.front]
        self.data[self.front] = None
        if self.count == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        self.count -= 1
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self.data[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def __repr__(self):
        if self.is_empty():
            return "FRONT -> <- REAR"
        items = [str(self.data[(self.front + i) % self.size]) for i in range(self.count)]
        return "FRONT -> " + " -> ".join(items) + " <- REAR"



def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Enqueue (Add to Rear)")
    print("\n\t\t2. Dequeue (Remove from Front)")
    print("\n\t\t3. Peek Front")
    print("\n\t\t4. Display Queue")
    print("\n\t\t5. Size / Check Empty / Check Full")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def main():
    print("\n\t\tEnter queue capacity (default 20): ", end="")
    cap_input = input().strip()
    try:
        cap = int(cap_input) if cap_input else 20
    except ValueError:
        cap = 20
    q = Queue(size=cap)
    print(f"\n\t\tQueue created with capacity {q.size}.")

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
            try:
                q.enqueue(value)
                print(f"\n\t\t'{value}' enqueued successfully!")
            except OverflowError:
                print("\n\t\tQueue is FULL! Cannot enqueue.")

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
            print(f"\n\t\tSize     : {q.count} / {q.size}")
            print(f"\n\t\tEmpty?   : {'Yes' if q.is_empty() else 'No'}")
            print(f"\n\t\tFull?    : {'Yes' if q.is_full() else 'No'}")

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")


main()