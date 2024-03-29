def two_array(a,b,n):
    res =0
    for i in range(0,n):
        sum_array_1 =0
        sum_array_2 =0
        for j in range(i,n):
            sum_array_1+=a[j]
            sum_array_2+=b[j]
            if sum_array_1 == sum_array_2:
                res = max(res,j-i+1)

    return res

a =[0,1,0,0,0,0]
b =[1,0,1,0,0,1]
n = len(a)
print(two_array(a,b,n))


#  time_complexity = O(n^2)

def two_array_Ea(a,b,n):
    res =0
    temp =[None]*n
    for i in range(0,n):
        temp[i]=a[i]-b[i]

    # return temp
    max_len =0
    dictonary = dict()
    sums =0
    for i in range(0,n):
        sums += temp[i] 
        if sums == 0:
            max_len = i+1
        if sums in dictonary:
            max_len = max(max_len , i-dictonary[sums])
        else:
            dictonary[sums] = i
    return max_len


a =[0,1,0,0,0,0]
b =[1,0,1,0,0,1]
n = len(a)
print(two_array_Ea(a,b,n))

