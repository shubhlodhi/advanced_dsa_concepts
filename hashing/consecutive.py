# a =[1,9,3,4,2,20]

def cosecutive(a,n):
    a1 = a.sort()
    res =0
    for i in range(1,n):
        if a[i]-1 == a[i-1]:
            res+=1

    return res+1


def consecutive_EA(a,n):
    set_a = set(a)
    x = a[0]
    res =0
    for i in range(0,n):
      if a[i]-1 not in set_a:
        result =0
        # res = a[i]
        for j in range(0,n):
           if (a[i]+j) in set_a:
            result+=1

        res = max(res,result)
      else:
         continue
    return res


           
        # x  = min(x,res)
    # for i in range(0,n):
    #    if x+i in set_a:
        # res+=1

    # return res



        # if a[i] in set_a:
            # if a[i]-1 in set_a:
                # x = a[i]-1
      
        # if x+1 in set:
            
            # res = max(res,)

        

#
a =[1,9,3,4,2,20]
# a =[10,20,30]
n = len(a)
print(consecutive_EA(a,n))
# print(3%8)