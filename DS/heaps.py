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
        # FIX: Append the new element to the end of the list
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
            lef = self._left_child(i)
            right = self._right_child(i)
            
            if lef < n and self.heap[lef] < self.heap[smallest]:
                smallest = lef
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest == i:
                break
                
            self._swap(i, smallest)
            i = smallest
            
    def heapify(self, arr):
        self.heap = arr[:]
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heapify_down(i)
            
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
        
        # Build the string for the current node
        result = prefix
        if prefix: # Only add branching symbols if it's not the root
            result += "└── " if is_last else "├── "
        result += str(self.heap[i]) + "\n"
        
        # Calculate the prefix for the children
        child_prefix = prefix + ("    " if is_last else "│   ")
        
        left = self._left_child(i)
        right = self._right_child(i)
        
        # Recursively build left and right children
        if left < len(self.heap):
            # The left child is only the "last" if there is no right child
            left_is_last = (right >= len(self.heap))
            result += self._build_tree_str(left, child_prefix, left_is_last)
            
        if right < len(self.heap):
            # The right child is always the "last" child of its parent
            result += self._build_tree_str(right, child_prefix, True)
            
        return result
        
    def delete(self):
        if self.isempty():
            print("empty heap")
            return None
        self._swap(0, len(self.heap) - 1)
        val_to_delete = self.heap.pop()
        self._heapify_down(0)
        return val_to_delete


# --- Test Cases ---
print("=== First Heap (Insertions) ===")
myheap = Heap()
for v in [5, 6, 6, 261, 6, 541, 6, 15, 12]:
    myheap.insert(v)
print(myheap)
print(f"Size: {myheap.size()}")
print(f"Is empty?: {myheap.isempty()}\n")

print("=== Second Heap (Heapify and Delete) ===")
myheap2 = Heap()
myheap2.heapify([581, 61, 61, 65, 1641, 613, 61, 785, 91, 1, 35, 64])
print("Before Delete:")
print(myheap2)

deleted_val = myheap2.delete()
print(f"Deleted value: {deleted_val}")
print("After Delete:")
print(myheap2)