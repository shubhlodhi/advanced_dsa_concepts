def sub_array(a,n,key):
    # res = 0
    for i in range(n):
        res =0
        for j in range(i,n):
            res+=a[j]
            if res == key:
                return True , f"{i} to {j}"
            
    return False

a =[1,4,20,3,10,5]
n = len(a)
print(sub_array(a,n,33))

# time commplexity = O(n^2)


# def sub_array_efficient(a,n,key):

