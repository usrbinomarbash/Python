def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1