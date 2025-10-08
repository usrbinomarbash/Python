def selectionSortAsc(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

mylst=[4,13,3,1,16]

def selectionSortDesc(arr):
    n=len(arr)
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if(arr[j]>arr[max_index]):
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]






selectionSortAsc(mylst)
print(mylst)
selectionSortDesc(mylst)
print(mylst)

