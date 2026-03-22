
import os


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if not self.head:
            return "None <-> None"
        s    = "None <-> "
        curr = self.head
        while curr:
            s   += f"{curr.data} <-> "
            curr = curr.next
        s += "None"
        return s


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev  = self.tail
        self.tail.next = new_node
        self.tail      = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next  = self.head
        self.head.prev = new_node
        self.head      = new_node

    def delete(self, target):
        if not self.head:
            print("\n\t\tLinked list is EMPTY!")
            return
        curr = self.head
        while curr:
            if str(curr.data) == str(target):
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next       # deleting head
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev       # deleting tail
                print(f"\n\t\t'{target}' was deleted successfully!")
                return
            curr = curr.next
        print(f"\n\t\t'{target}' was NOT FOUND in the list!")

    def search(self, target):
        curr  = self.head
        index = 0
        while curr:
            if str(curr.data) == str(target):
                return index
            curr = curr.next
            index += 1
        return -1

    def size(self):
        count = 0
        curr  = self.head
        while curr:
            count += 1
            curr   = curr.next
        return count

    def traverse_backward(self):
        if not self.tail:
            return "None <-> None"
        s    = "None <-> "
        curr = self.tail
        while curr:
            s   += f"{curr.data} <-> "
            curr = curr.prev
        s += "None"
        return s

    def create_from_file(self, filename):
        if not os.path.exists(filename):
            print(f"\n\t\tSORRY! Could not open '{filename}'!")
            return
        with open(filename, 'r') as f:
            for line in f:
                value = line.strip()
                if value:
                    self.append(value)
        print(f"\n\t\tLinked list created from '{filename}' successfully!")


# ── Menu ──────────────────────────────────────────────────────────────────────

def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Create List from File")
    print("\n\t\t2. Add a New Node")
    print("\n\t\t3. Delete a Node")
    print("\n\t\t4. Traverse the Linked List")
    print("\n\t\t5. Search / Backward Traverse / Size")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def sub_menu_5(ll):
    print("\n\t\t  --- Extra Options ---")
    print("\n\t\t  a. Search for a value")
    print("\n\t\t  b. Traverse backward (tail -> head)")
    print("\n\t\t  c. Count nodes")
    print("\n\t\t  Choice: ", end="")
    sub = input().strip().lower()
    if sub == 'a':
        print("\n\t\tEnter value to search: ", end="")
        target = input().strip()
        idx    = ll.search(target)
        if idx == -1:
            print(f"\n\t\t'{target}' was NOT FOUND in the list!")
        else:
            print(f"\n\t\t'{target}' was FOUND at index {idx}!")
    elif sub == 'b':
        if not ll.tail:
            print("\n\t\tLinked list is EMPTY!")
        else:
            print("\n\t\tBackward traversal (tail -> head):")
            print(f"\n\t\t{ll.traverse_backward()}")
    elif sub == 'c':
        print(f"\n\t\tThe list has {ll.size()} node(s).")
    else:
        print("\n\t\tInvalid sub-option!")


def main():
    ll = DoublyLinkedList()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-6.")
            continue

        if choice == 1:
            print("\n\t\tEnter filename: ", end="")
            filename = input().strip()
            ll.create_from_file(filename)

        elif choice == 2:
            print("\n\t\tAdd to (h)ead or (t)ail? ", end="")
            pos = input().strip().lower()
            print("\n\t\tEnter value to add: ", end="")
            value = input().strip()
            if pos == 'h':
                ll.prepend(value)
                print(f"\n\t\t'{value}' added to the head successfully!")
            elif pos == 't':
                ll.append(value)
                print(f"\n\t\t'{value}' added to the tail successfully!")
            else:
                print("\n\t\tInvalid position! Use 'h' or 't'.")

        elif choice == 3:
            print("\n\t\tEnter value to delete: ", end="")
            target = input().strip()
            ll.delete(target)

        elif choice == 4:
            if not ll.head:
                print("\n\t\tLinked list is EMPTY!")
            else:
                print("\n\t\tForward traversal (head -> tail):")
                print(f"\n\t\t{ll}")

        elif choice == 5:
            sub_menu_5(ll)

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")


main()