
def selection_sort(arr):
    assignments=0
    comparisons=0
    for i in range(len(arr)):
        min_index=i
        assignments=assignments+1
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min_index]):
                min_index=j
                assignments=assignments+1
            comparisons=comparisons+1# indented wrong unindented i incremented whenever even i didn't do the comparisons
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        assignments=assignments+3
    return( str(arr)+" \n selection sort array has made: "+ str(comparisons)+" comparisons and "+ str(assignments)+" assignments")

def bubble_sort(arr):
    assignments=0
    comparisons=0
    for i in range(len(arr)):
        #for i=0 i<n-1 i= i+=1
        for x in range(len(arr)-i-1):
            if(arr[x]>arr[x+1]):
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
                assignments=assignments+3
            comparisons = comparisons + 1

    return " bubble sort has done: "+str(comparisons)+" comparisons and "+ str(assignments)+" assignments"

mylis=[i for i in range(100)]#worst case

print(selection_sort(mylis)) # ascending and we so we were sorting ascending
print(bubble_sort(mylis)) # worst case descending and we were sorting ascending so this triggered

# bubble sort does not affect the runtime of no matter how scrambled it is it is always  once it finds the max the min it knows how to behave after  this one knows where to shift everyone after the first pass
# selection sort adapts to the arrangement or disarrangement of the array   this one doesn't where to shift everyone after the first pass

def heap_sort(arr):
    n = len(arr)
    assignments = 0
    comparisons = 0

    def left_child(i):
        return 2 * i + 1

    def right_child(i):
        return 2 * i + 2

    def last_parent(n):
        return (n-1)//2

    def sift_down(i, heap_size):
        nonlocal assignments, comparisons

        largest = i
        left = left_child(i)
        right = right_child(i)

        # Compare with left child
        if left < heap_size:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        # Compare with right child
        if right < heap_size:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        # Swap if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            assignments += 2  # Each swap = 2 assignments
            sift_down(largest, heap_size)

    # Step 1: Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        assignments += 2

        # Heapify the reduced heap
        sift_down(0, i)  # heap_size is now i (excluding sorted elements)

    return arr, assignments, comparisons


# Test it
arr = [4, 10, 3, 5, 1, 8, 7]
sorted_arr, assignments, comparisons = heap_sort(arr)
print(f"Sorted Heapifed Array: {sorted_arr}")
print(f"Assignments: {assignments}")
print(f"Comparisons: {comparisons}")