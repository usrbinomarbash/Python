def insertion_sort(A):
    comparisons=0
    assignments=0
    for i in range(1,len(A)):
        current=A[i]
        j=i-1
        while(j>=0 and A[j]>current):
            A[j+1]=A[j]
            j-=1
            comparisons+=1
            assignments+=1
        '''
        swap version
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # swap
            j -= 1
        '''
        A[j+1]=current
        assignments+=1
    return f"The Array: {A} \nhas done: {comparisons} comparisons and {assignments} assignments \n and a total of: {assignments+comparisons} operations"
myarr=[47, 3, 89, 12, 56, 7, 91, 23, 5, 68]
print(insertion_sort(myarr))





def insertion_sortA(arr):
    comparisons=0
    assignments=0

    for k in range(1,len(arr)):
        current=arr[k]
        j=k-1
        while(j>=0 and arr[j]>current):
            arr[j+1]=arr[j]
            j-=1
            comparisons=comparisons+1
            assignments=assignments+1
        if(j>=0):
            comparisons+=1
        arr[j+1]=current
        assignments+=1
    return(f"Here is the insertion_sort: {arr} and it has done: {comparisons} comparisons and {assignments} assignments a total of: {assignments+comparisons} operations onit")

print(insertion_sortA([851,51,6,15,67,17,8,12,56]))