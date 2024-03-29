def n_k_times(a,n,k):
    b = [0]*n
    for i in range(0,n):
        b[a[i]] +=1

    for i in range(n):
        if b[i] >n/k:
            print(i)

# def n_k_times(a,n,k):


a =[3,1,2,2,1,2,3,3]
n= len(a)
print(n_k_times(a,n,4))
        

