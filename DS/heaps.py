# ── Min-Heap ──────────────────────────────────────────────────────────────────


class Heap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return (2 * i) + 1

    def _right_child(self, i):
        return (2 * i) + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, m):
        self.heap.append(m)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0:
            par = self._parent(i)
            if self.heap[i] < self.heap[par]:
                self._swap(i, par)
                i = par
            else:
                break

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            lef      = self._left_child(i)
            right    = self._right_child(i)
            if lef   < n and self.heap[lef]   < self.heap[smallest]: smallest = lef
            if right < n and self.heap[right] < self.heap[smallest]: smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def heapify(self, arr):
        self.heap = arr[:]
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heapify_down(i)

    def delete_min(self):
        if self.isempty():
            return None
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._heapify_down(0)
        return val

    def peek_min(self):
        if self.isempty():
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def isempty(self):
        return len(self.heap) == 0

    def __repr__(self):
        return f"MinHeap({self.heap})"

    def __str__(self):
        if self.isempty():
            return "Empty Heap"
        return self._build_tree_str(0, "", True)

    def _build_tree_str(self, i, prefix="", is_last=True):
        if i >= len(self.heap):
            return ""
        result = prefix
        if prefix:
            result += "└── " if is_last else "├── "
        result += str(self.heap[i]) + "\n"
        child_prefix = prefix + ("    " if is_last else "│   ")
        left         = self._left_child(i)
        right        = self._right_child(i)
        if left < len(self.heap):
            left_is_last = (right >= len(self.heap))
            result += self._build_tree_str(left,  child_prefix, left_is_last)
        if right < len(self.heap):
            result += self._build_tree_str(right, child_prefix, True)
        return result


# ── Menu ──────────────────────────────────────────────────────────────────────

def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Insert a Value")
    print("\n\t\t2. Delete Minimum (Root)")
    print("\n\t\t3. Peek Minimum")
    print("\n\t\t4. Display Heap")
    print("\n\t\t5. Heapify from a List")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def main():
    h = Heap()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-6.")
            continue

        if choice == 1:
            print("\n\t\tEnter integer value to insert: ", end="")
            try:
                value = int(input().strip())
                h.insert(value)
                print(f"\n\t\t{value} inserted into the heap!")
            except ValueError:
                print("\n\t\tInvalid value! Please enter an integer.")

        elif choice == 2:
            val = h.delete_min()
            if val is None:
                print("\n\t\tHeap is EMPTY! Nothing to delete.")
            else:
                print(f"\n\t\tMinimum value {val} deleted from the heap!")

        elif choice == 3:
            val = h.peek_min()
            if val is None:
                print("\n\t\tHeap is EMPTY!")
            else:
                print(f"\n\t\tMinimum (root): {val}")

        elif choice == 4:
            if h.isempty():
                print("\n\t\tHeap is EMPTY!")
            else:
                print(f"\n{h}")
                print(f"\n\t\tSize: {h.size()}")

        elif choice == 5:
            print("\n\t\tEnter space-separated integers to heapify: ", end="")
            raw = input().strip()
            try:
                arr = list(map(int, raw.split()))
                h.heapify(arr)
                print(f"\n\t\tHeapified successfully!")
                print(f"\n{h}")
            except ValueError:
                print("\n\t\tInvalid input! Please enter integers only.")

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")


main()