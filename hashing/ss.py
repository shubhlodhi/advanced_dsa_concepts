def count_1_0_equal_pair_RA(a,n):
   for i in range(0,n):
      if a[i] == 0:
         a[i]= -1

   dictionary = dict()
   sum =0
#    dictionary[sum] = 1
   result =0

   for i in range(0,n):
     sum+=a[i]
    #  a[i] = sum
    #  frequency= sum
     if sum not in dictionary:
        #  dictionary[sum] = dictionary.get(sum,0)+1
         dictionary[sum] = 1


     if sum in dictionary:
        result += dictionary[sum] 
        # result -=1
        # print(result)
        dictionary[sum] +=1
        # return dictionary
        
    #  return 
   return result
#    return a
#    return dictionary


#    return dictionary

    # dictionary[sum] +=1
    

         
#    return a


a = [1,0,0,1,0,1,1]
n  = len(a)
print(count_1_0_equal_pair_RA(a,n))

# a  = {1:2}
# print(a[1])


    