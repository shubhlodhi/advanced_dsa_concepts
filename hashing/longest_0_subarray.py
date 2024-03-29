def longest_subarray_0(a,n):
    for i in range(0,n):
        if a[i] ==0:
            a[i] = -1

    pre_sum=0
    res=0
    dictonary = dict() 
    for i in range(n):
        pre_sum+=a[i]
        if pre_sum ==0:
            res  = i+1

        if pre_sum  in dictonary:
            res = max(res,i-dictonary[pre_sum])

        else:
            dictonary[pre_sum] = i

    return res


a =[1,0,1,1,1,0,0]
n = len(a)
print(longest_subarray_0(a,n))

        



        