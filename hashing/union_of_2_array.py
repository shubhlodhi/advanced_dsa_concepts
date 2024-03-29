def union(a,b):
    len_a  = len(a)
    len_b = len(b)
    set_a = set(a)
    set_b = set(b)
    n = len(set_a)
    res =0
    for i in range(len_b):
        for j in range(len_a):
            if a[j] == b[i]:
                res+=1
                a.pop(i)

    return res
a =[10,15,20,5,30]
b = [30,5,30,80]
print(union(a,b))
        
        