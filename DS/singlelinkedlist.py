# ── Singly Linked List ────────────────────────────────────────────────────────
import os


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head     = None
        self.tail     = None
        self.circular = False

    def __repr__(self):
        if not self.head:
            return "HEAD -> None"
        s    = "HEAD -> "
        curr = self.head
        while curr.next and curr.next != self.head:
            s   += f"{curr.data} -> "
            curr = curr.next
        s += f"{curr.data}"
        s += " -> (back to HEAD)" if self.circular else " -> None"
        return s

    # ── Core Operations ───────────────────────────────────────────────────────

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            if self.circular:
                self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail      = new_node
        if self.circular:
            self.tail.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            if self.circular:
                self.tail.next = self.head
            return
        new_node.next = self.head
        self.head     = new_node
        if self.circular:
            self.tail.next = self.head

    def delete(self, target):
        if not self.head:
            print("\n\t\tLinked list is EMPTY!")
            return

        stop = self.head if self.circular else None

        # only node
        if self.head == self.tail:
            if str(self.head.data) == str(target):
                self.head = self.tail = None
                print(f"\n\t\t'{target}' was deleted successfully!")
                return
            else:
                print(f"\n\t\t'{target}' was NOT FOUND in the list!")
                return

        # target is head
        if str(self.head.data) == str(target):
            self.head = self.head.next
            if self.circular:
                self.tail.next = self.head
            print(f"\n\t\t'{target}' was deleted successfully!")
            return

        curr = self.head
        while curr.next and curr.next != stop:
            if str(curr.next.data) == str(target):
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                if self.circular:
                    self.tail.next = self.head
                print(f"\n\t\t'{target}' was deleted successfully!")
                return
            curr = curr.next

        print(f"\n\t\t'{target}' was NOT FOUND in the list!")

    def search(self, target):
        if not self.head:
            return -1
        curr  = self.head
        index = 0
        stop  = self.head if self.circular else None
        while curr:
            if str(curr.data) == str(target):
                return index
            curr = curr.next
            index += 1
            if curr == stop:
                break
        return -1

    def size(self):
        if not self.head:
            return 0
        count = 0
        curr  = self.head
        stop  = self.head if self.circular else None
        while curr:
            count += 1
            curr   = curr.next
            if curr == stop:
                break
        return count

    def reverse(self):
        if self.circular:
            self.tail.next = None         # temporarily break circle
        prev      = None
        curr      = self.head
        self.tail = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev      = curr
            curr      = next_node
        self.head = prev
        if self.circular:
            self.tail.next = self.head    # restore circle

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

    # ── Circular Operations ───────────────────────────────────────────────────

    def make_circular(self):
        if not self.head:
            print("\n\t\tLinked list is EMPTY! Cannot make circular.")
            return
        if self.circular:
            print("\n\t\tList is ALREADY circular!")
            return
        self.tail.next = self.head
        self.circular  = True
        print("\n\t\tList is now CIRCULAR! Tail points back to Head.")

    def break_circular(self):
        if not self.circular:
            print("\n\t\tList is NOT circular!")
            return
        self.tail.next = None
        self.circular  = False
        print("\n\t\tCircular link BROKEN! List is now linear.")

    def is_circular(self):
        """Verify with Floyd's Cycle Detection (tortoise and hare)."""
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# ── Menu ──────────────────────────────────────────────────────────────────────

def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Create List from File")
    print("\n\t\t2. Add a New Node")
    print("\n\t\t3. Delete a Node")
    print("\n\t\t4. Traverse the Linked List")
    print("\n\t\t5. Search / Reverse / Size")
    print("\n\t\t6. Circular Operations")
    print("\n\t\t7. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def sub_menu_5(ll):
    print("\n\t\t  --- Extra Options ---")
    print("\n\t\t  a. Search for a value")
    print("\n\t\t  b. Reverse the list")
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
        ll.reverse()
        print("\n\t\tList reversed successfully!")
        print(f"\n\t\t{ll}")
    elif sub == 'c':
        print(f"\n\t\tThe list has {ll.size()} node(s).")
    else:
        print("\n\t\tInvalid sub-option!")


def sub_menu_6(ll):
    print("\n\t\t  --- Circular Options ---")
    print("\n\t\t  a. Make Circular")
    print("\n\t\t  b. Break Circular")
    print("\n\t\t  c. Check if Circular (Floyd's Algorithm)")
    print("\n\t\t  Choice: ", end="")
    sub = input().strip().lower()
    if sub == 'a':
        ll.make_circular()
    elif sub == 'b':
        ll.break_circular()
    elif sub == 'c':
        result = ll.is_circular()
        print(f"\n\t\tList is {'CIRCULAR' if result else 'NOT circular'}! (Floyd's Detection)")
    else:
        print("\n\t\tInvalid sub-option!")


def main():
    ll = SinglyLinkedList()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-7.")
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
                print("\n\t\tTraversing the list:")
                print(f"\n\t\t{ll}")

        elif choice == 5:
            sub_menu_5(ll)

        elif choice == 6:
            sub_menu_6(ll)

        elif choice == 7:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-7.")


main()
