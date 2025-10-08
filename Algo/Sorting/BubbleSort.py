def bubbleSortAscending(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def bubbleSortDescending(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]<arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

mylst2=[12,51,51,1,4,3]
bubbleSortAscending(mylst2)
print(mylst2)

bubbleSortDescending(mylst2)
print(mylst2)