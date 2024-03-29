def dis_ele(a,n ,k):
    for i in range(n):
        if k >n:
            break
        a1 =[]
        # a1_set = set
        for j in range(i,k):
            a1.append(a[j])

        a1_set =set(a1)
        # a2 = set(a1_set)
        print(len(a1_set))
        # res =0
        # a2 =[]
        # for k in range(len(a1_set)):
            # res+=1
        # print(res)
        # a2.append(res)
        k+=1
        # print(len(a1_set))
        # a1_set = ()
    # return a1

def gfg_apporach(a,n ,k):
    for i in range(0,k):
        print(len(set(a[i:i+k])))

def efficient_approach(a,n):
    d = dict()
    k =4
    for i in range(0,k):
        present_value = a[i]
        if present_value in d:
        # d[a[i]] +=1
         d[present_value]+=1 

        else:
            d[a[i]] = 1

    print(len(d))

    i= 0
    for j in range(k,n):
        present_value = a[j]
        first_value = a[i]

        if present_value in d:
            d[present_value]+=1
            d[first_value] -=1
            print(len(d))
            

        else:
            d[present_value] = 1
            d[first_value] -=1
            print(len(d))

        i+=1
    return d
    





    return len(d)
a =[10,20,20,10,30,40,10]
n =len(a)
# print(dis_ele(a,n,4))
print(efficient_approach(a,n))
# print((10%6)%6)


