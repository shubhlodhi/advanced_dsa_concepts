def rotation(a,b):
    flag = False
    for i in range(0,len(b)):
        for j in range(i+1,len(a)):
            if b[i] == a[j]:
                k = i+1
                for f in range(j+1, len(a)):
                    if b[k] != a[f]:
                        flag  = True
                        # print(k)
                        # return k
                    k+=1

                if flag != True:
                    j =0
                    for i in range(k,len(a)):
                        if a[i] != a[j]:
                            flag = True

                    

                        j+=1

                    else:
                        return flag

    # return flag




            

a = "mightandmagic"
b = "andmagicmigth"
print(rotation(a,b))
