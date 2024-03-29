import math
def repeating_charL(a):

    dict1 = dict()
    res =math.inf
    for i in range(len(a)):
        if a[i] not in dict1:

         dict1[a[i]] = i

        # if a[i] in dict1:
        else:
           
           res = min(res,dict1[a[i]])
        #    return res
           dict1[a[i]]  =i

    return res


a = "heksforgks"
print(repeating_charL(a))
