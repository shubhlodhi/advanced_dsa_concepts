def palindrome(a,n):
    i= 0
    j =n-1
    k = n-1
    while i<j:
        if a[i] == a[j]:
            i+=1
            j-=1
        if a[i] != a[j]:
            for z in range(0,n):
                if a[i]!=a[k]:
                    k-=1

                else:
                    break 
            # (a[j]),(a[k]) = a[k],a[j]



    return k

def check_palindrome(a,n):
    a1 = [0]*n
    for i in range(0,n):

        # a1[ord(a[i])]+=1
        s = ord(a[i])%n
        a1[s]+=1

        # a1.append(s)
    for i in range(0,n):
        if a1[i]%2 != 0:
            return False


    return True
        
    return a1
a = "geek"
n =len(a)
print(check_palindrome(a,n))
# print(94%5)