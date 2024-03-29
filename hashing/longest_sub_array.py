def longest_subarray(a,n):
    
    for i in range(0,n):
        res = 0
        res_impoortant = 0
        for j in range(i,n):
         res+=a[j]
         res_impoortant+=1

         if res == 5:
            return res_impoortant
    return -1
def longest_subarray(a,n):
    res2 =0
    for i in range(0,n):
        res = 0
        # res_impoortant = 0
        for j in range(i,n):
         res+=a[j]
        #  res_impoortant+=1

         if res == 5:
            res2 = max(res2,j-i+1)
            break
           
          # return res_impoortant
    

a =[3,1,0,1,8,2,3,6]
n =len(a)
print(longest_subarray(a,n))