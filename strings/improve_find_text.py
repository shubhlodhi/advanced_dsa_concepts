def improve_naive_find_pattern(a,p,n,np):
    i =0
    while i<=n-np+1:
        

        j =0
        while j<np:
            if a[i+j] != p[j]:
                if i>j:
                 i =j
                # print(i)
                # if j<i:
                break
            j+=1
        

            # if j == np:
            #  print(i ,end="")
        # i+=1

a = "ABABABAB"
p = "ABAB"
n = len(a)
np = len(p)
print

improve_naive_find_pattern(a,p,n,np)

