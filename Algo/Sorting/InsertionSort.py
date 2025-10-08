def insertion_sort_ascending(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1,len(arr)):
        key=arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort_ascending([4, 41, 21, 12, 3]))
def insertion_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1,len(arr)):
        key=arr[i]
        j = i-1
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort_descending([4, 41, 21, 12, 3]))
