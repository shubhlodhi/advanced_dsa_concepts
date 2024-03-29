def rotated_string(a,b,n):
    
    # last_item = a[n-1]
    # for i in range(n-1,-1,-1):
    # i =n-1
    # while i>n-2:
        # last_item = a[0]
        # a[i-1] = a[i]
    if a[n-1] != b[n-3]:
        return False

    else:
        return True
            # i -=1
            # return False

        # i-=1




    # a[n-1] = last_item

    # return a

a = "geeksforgeeks"
b = "eksforgeeksge"
n =len(a)
print(rotated_string(a,b,n))