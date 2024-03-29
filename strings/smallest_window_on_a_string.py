import math


def smallest(a,p):
    dictq = dict()
    for i in range(len(p)):
        dictq[p[i]] = 1
    for i in range(0,len(a)):
        t1 =0
        for  j in range(i,len(a)):
            if a[j] in dictq:
                dictq[a[j]]+=1
                t1+=1
                if dictq[a[j]] >=2:
                    i = j
                    break
                
                if t1 == 3:
                    print(i ,"to" ,j)

def smaleest_0(a,p):
    res =math.inf
    for i in range(0,len(a)):
        k =0
        # f = ""
        

        for j in range(i,len(a)):
            if a[j] == p[k]:
                k+=1
                if k == 3:
                    # return(i ,"to" ,j)

                    
                    mini = abs(i-j+1)
                    res= min(res , mini)
                    f = a[i:j+1]
                    break
            if a[j] != p[k]:
                break

    return res 
    



                    # return f
                    


                    # break
a = "zoomlazapzo"
p = "oza"
print(smaleest_0(a,p))


                

                
                    

        