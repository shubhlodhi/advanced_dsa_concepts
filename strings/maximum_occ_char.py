def occ_ele(a,n):
    count = [0]*256

    for i in range(0,n):
        count[ord(a[i])] +=1

    maxi = max(count)
    for j in range(0,len(count)):
        if count[j] == maxi:
            return chr(j)

            # print(chr(j))
            # return maxi


a = "TESTSAMPLE"
n = len(a)
print(occ_ele(a,n))


