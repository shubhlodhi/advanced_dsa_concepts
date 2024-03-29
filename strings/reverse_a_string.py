a = "i.like.this.program.very.much"
d = len(a)
print(d)
s = a.split("."  )
s.reverse()
print(s)
def reverse_string(a,n):
    temp = ""
    i =n-1
    # for i in range(n-1,-1,-1):
    while i>=0:

        # if a[i] == ">":
            temp = (a[i])
            i-=1
        # print(a[i],end="")
        # i-=1

    return temp
    # string = a.split

a = "HELLO . sir"
n = len(a)
print(reverse_string(a,n))

# a = "i love programming very much"
# # s = list(a)
# n = len(a)
# # print(s)
# temp =[]
# for i in range(n-1,-1,-1):
       
#        s= list(a)
#        if a[i] == " " or i == 0:
#              temp.append(a[i:n])

#              n = i 

# # temp1 = str(temp)
# for i in range(len(temp)):
#       print(temp[i],end="")
# temp.append(a[i:n])
# print(temp1)


def ss(a,n):
      for i in range(n-1,-1,-1):
            if a[i] == " " or i == 0:
                  print(a[i:n] ,end=" ")
                  n = i


a = "i love programming very much"
# s = list(a)
n = len(a)
ss(a,n)

