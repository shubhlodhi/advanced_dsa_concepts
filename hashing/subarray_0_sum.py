# def sum_0(a,n):
#     for i in range(0,n):
#         res =0
#         for j in range(i,n):
#             res+=a[j]
#             if res == 0:
#                 return f" index {i} to {j} = 0"

#     return -1


# def pre_sum(a,n):
#     a1 =[]
#     sum = a[0]
#     for i in range(1,n):
#         sum = (sum - a[i])
#         a1.append(sum) 
#     # return a1
  
        
#     return False

def pre_sum2(a,n):
    pre_sum =0
    h = set()
    for i in range(n):
        pre_sum+=a[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        else:
            h.add(pre_sum)







a =[1,4,13,-3,-10,5]
n = len(a)
print(pre_sum2(a,n))