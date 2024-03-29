def count_1_0_equal_pair(a,n):
    res =0
    for i in range(0,n):
        zer0 =0
        on1 = 0
        for j in range(i,n):
            if a[j] == 0:

             zer0+=1
             if zer0 == on1:
                res+=1

            if a[j] == 1:
             on1+=1
             if zer0 == on1:
                res+=1
    return res

a =[1,0,0,1,0,1,1]
n = len(a)
print(count_1_0_equal_pair(a,n))
#   time complexity = O(n^2)



#  efficient_approach:

# print(-1+(1))
def count_1_0_equal_pair_RA(a,n):
   for i in range(0,n):
      if a[i] == 0:
         a[i] = -1

   dictionary = dict()
   sum =0
   dictionary[sum] = 1
   result =0

   for i in range(0,n):
     sum+=a[i]
     if sum not in dictionary:
         dictionary[sum] =1


     if sum in dictionary:
        result += dictionary[sum]
        # print(result)
        dictionary[sum] +=1
        # return dictionary
        
    #  return 
#    return result
   return dictionary


#    return dictionary

    # dictionary[sum] +=1
    

         
#    return a


a = [1,0,0,1,0,1,1]
n  = len(a)
print(count_1_0_equal_pair_RA(a,n))

# a  = {1:2}
# print(a[1])


    