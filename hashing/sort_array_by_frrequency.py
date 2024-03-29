def dd(a,n):
    dicton = dict()
    for i in range(0,n):
        sum =a[i]
        if sum in dict:
            dicton[sum] +=1

        else:
            dicton[sum] = 1
    maximum = max(a)
    array = [0]*maximum
    # for i in range(0,n):


# a ={"ss" :1 , "ll":2}

# pending question
# print(list(a.values().index(1)))