#Min Heap
class Heap:
    def __init__(self):
        self.heap=[]
    
    def _parent(self,i):
        return (i-1)//2
    
    def _left_child(self,i):
        return((2*i)+1)

    def _right_child(self,i):
        return((2*i)+2)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, i):
        self.heap.append(i)
        self._heapify_up(len(self.heap) -1)
    
    def _heapify_up(self,i):
        while(i>0):
            par = self._parent(i)
            if(self.heap[i] <self.heap[par]):
                self._swap(i, par)
                i=par
            else:
                break
    
    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            lef=self._left_child(i)
            right=self._right_child(i)
            if(lef<n and self.heap[lef]<self.heap[smallest]):
                smallest=lef
            if(right<n and self.heap[right]<self.heap[smallest]):
                smallest=right
            if smallest == i:
                break
            self._swap(i, smallest)
            i=smallest
    def heapify(self, arr):
        self. heap= arr[:]
        for i in range((len(self.heap)-2) // 2,-1,-1):
            self._heapify_down(i)
    def size(self):
        return len(self.heap)
    
    def isempty(self):
        if(len(self.heap)==0):
            return True
        return False
    def __repr__(self):
        return(f"MinHeap({self.heap})")
    def delete(self):
        if self.isempty():
            print("empty heap")
        self._swap(0, len(self.heap)-1)
        val_to_delete=self.heap.pop()
        self._heapify_down(0)
        return val_to_delete

myheap = Heap()
for v in [5,6,6,261,6,541,6,15,12]:
    myheap.insert(v)
print(myheap)
print(myheap.size())
print(myheap.isempty())

myheap2 = Heap()
myheap2.heapify([581,61,61,65,1641,613,61,785,91,1,35,64])
myheap2.delete()
print(myheap2)
