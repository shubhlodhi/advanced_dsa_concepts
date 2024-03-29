# def pair_sum(a,n ,key):
    # for i in range(0,n):
        # for j in range (i,n):
            # if a[i]+a[j] == key:
                # return True

    # return False

def pair_sum(a,n,key):
    i= 0
    j =1
    while i<n:
        if j>=n:
            return True
        if a[i]+a[j] == key:
            return True
        if a[i]+a[j]<key:
            i+=1
        else:
            j+=1

    return False



    
a =[ 5,8,-3,6]
n  =len(a)
print(pair_sum(a,n,3))
