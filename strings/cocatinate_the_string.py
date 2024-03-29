# a = "klpo"
# b= "klop"
# c= a+b
# print(c)
def concatinate(a,b ):

    count = [0]*256
    c = a+b
    m = len(c)
    for i in range(m):
        # if count[ord(a[i])] == 1:
            count[ord(c[i])] += 1
        # count[ord(a[i])] = 1


    # for i in range(m):
        # if count[ord(b[i])] == 1:
            # count[ord(b[i])] +=1
        # count[ord(b[i])] = 1
        # count[ord(b[i])]+=1

    for i in range((len(count))):
        if count[i] == 1:
            print(chr(i) ,end="")
    # print(count)
a = "aacdb"
n =len(a)

b = "gafd"
m = len(b)
print(concatinate(a,b))



        