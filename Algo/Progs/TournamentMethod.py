## BAse Case 2 elements

def tournament_method(arr):
    n=len(arr)
    for i in range(n):
        if(len(arr)==2):
            if(arr[1]>arr[0]):
                return arr[1]
            else:
                return arr[0]
    else:
        if(arr[i]>arr[i+1]):
            arr[i+1]=arr[i]
        else:
            arr[i]=arr[i+1]
           