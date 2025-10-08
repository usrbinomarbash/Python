def second_max(myarr):
    max=myarr[0]
    second_max=myarr[1]
    if(second_max > max):
        max, second_max=second_max,max
    for i in range(2, len(myarr)):
        if(myarr[i] > max):
            second_max=max
            max=myarr[i]
        elif(myarr[i]<max and myarr[i]>second_max):
            second_max=myarr[i]
    return second_max