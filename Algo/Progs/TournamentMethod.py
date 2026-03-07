## BAse Case 2 elements

def tournament_method(arr):
    n=len(arr)
    comparisons=0
    assignments=0
    if(n==1):
        return arr[0]
    if (n == 2):
        if (arr[1] > arr[0]):
            comparisons+=1
            return arr[1]
        else:
            return arr[0]
    winners=[]
    for i in range(0,n-1,2):
        comparisons += 1
       if(arr[i] > arr[i+1]):
           winners.append(arr[i])
       else:
           comparisons+=1
            winners.append(arr[i+1])
    if(n%2==0):
        winners.append(arr[-1])
    result= tournament_method(winners)
           