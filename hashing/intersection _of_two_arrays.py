def intersection(a,b):
    a_len = len(a)    
    b_len = len(b)
    res =0
    for i in range(0,a_len):
        flag  = False
        for j in range(i):

            if a[j] == a[i]:
                flag = True
                break

        if flag == True:
             continue
    # for i in range(a_len):
        for k in range(0,b_len):
           if a[i] == b[k]:
              res+=1

              break
    return res
# a = [10,5,20,5,30]
# b = [30,5,30,80]
a = [10,10,10,10]
b = [10,10,10]


print(intersection(a,b))



