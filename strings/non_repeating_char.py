def non_repeating(a,n):
    # for i in range(0,n):
    #     for j in range(i,n):
    #         if a[i] == a[j]:
    #             break

    #     if a[i] != a[j]:
    #         return chr(j)
    count = [False]*256
    for i in range(0,n):
        count[ord(a[i])]  = True

        for j in range(i+1,n):
            if a[j] == a[i]:
                count[ord(a[i])] = False


        if count[ord(a[i])] == True:
            return True , a[i]
        
    return False
        




            # else:
        # else:
            # print(chr(a[i]))
                # print(i)


a = "HELLO"
n = len(a)
print(non_repeating(a,n))