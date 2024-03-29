def subarray_with_sum(a,n,sum):
    res= 0
    for i in range(0,n):
        sums =0
        for j in range(i,n):
            sums+=a[j]
            if sums == sum:
                res+=1


    return res

a =[10,2,-2,-20,10]
n = len(a)
print(subarray_with_sum(a,n,-10))

