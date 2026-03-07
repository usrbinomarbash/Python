def partitionarray(A, element_to_partition):
    idx_of_parti=A.index(element_to_partition)
    pivot = A[idx_of_parti]
    B=[]
    for x in A:
        if x<pivot:
            B.append(x)

    B.append(pivot)
    for x in A:
        if x>pivot:
            B.append(x)
    return B
    
print(partitionarray([ 3,7,8,6,9,2,4,10,5], 5))