def tournament_method(arr, left,right):
    if(len(arr)==1):
        return arr[0]
    elif(len(arr)==2):
        if(arr[1]>arr[0]):
            return arr[1]
        else:
            return arr[0]
    else:
        mid= (left+right)//2
        round1=tournament_method(arr,left,mid)
        round2=tournament_method(arr,mid+1,right)
        return max(round1,round2)