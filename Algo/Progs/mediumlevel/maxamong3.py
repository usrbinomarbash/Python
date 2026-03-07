comp = 0
def max_VAL(A):
    global comp
    max_NUM=A[0]
    for i in range(0,len(A)):
        comp+=1
        if(A[i]>max_NUM):
            max_NUM=A[i]
    return max_NUM


def min_val(B):
    global comp
    min_num=B[0]
    for i in range(0,len(B)):
        comp+=1
        if(B[i]<min_num):
            min_num=B[i]
    return min_num
print(f"the max: {max_VAL([5,7,2])} and the number of comps:{comp}")

print(f"the min: {min_val([5,7,2])} and the number of comps:{comp}")

def econd_max(C):
    max=C[1]
    second_max=C[2]
    for j in range(len(C)):
        if C[j] > max:
            second_max = max
            max = C[j]
        elif (C[j] > second_max and C[j]<max):
            second_max=C[j]
    return second_max,max
print(econd_max([4,8,1,21,321,31,24,131]))


def min_and_max(C):
    min_num=C[0]
    max_num=C[len(C)-1]
    for i in range(len(C)):
        if(C[i]>max_num):
            max_num=C[i]
        elif(C[i]<min_num):
            min_num=C[i]
    return min_num,max_num
print(min_and_max([2,10,5]))

def tournament_method(D):
    while(len(D) > 1):
        winners=[]
        for i in range(0,len(D),2):
            if(i+1 < len(D)):
                if(D[i]>D[i+1]):
                    winners.append(D[i])
                else:
                    winners.append(D[i+1])
            else:
                winners.append(D[i])
        D= winners
    return D[0]

def secmax_and_max(L):
    max_inL=L[0]
    sec_max = L[1]
    for i in range(len(L)):
        if(L[i]>max_inL):
            sec_max=max_inL
            max_inL=L[i]
        elif(L[i]<max_inL and L[i]>sec_max):
            sec_max=L[i]
    return max_inL,sec_max
print(tournament_method([11,9,24,4]))
print(secmax_and_max([2,4,8,191,14,21]))

def tournammin(E):
    while(len(E)>2):
        J=[]
        for i in range(0,len(E),2):
            if(i+1<len(E)):
                if(E[i]<E[i+1]):
                    J.append(E[i])
                else:
                    J.append(E[i+1])
            
    return J[0]
print(tournammin([12,7,14,9]))