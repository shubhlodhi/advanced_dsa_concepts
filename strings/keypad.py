d = { "a" :2,"b":2 , "c":2 , "d" : 3,"e":3,"f":3 ,"g":4 ,"h":4 , "i":4}

a = "ghiabc"
# for i in range(0,len(a)):
#     if a[i] in d.keys():
#         print(d[a[i]], end="")



for i in range(0,len(a)):
    if ord(a[i]) >= ord("a") and ord(a[i])<=ord("c"):
        print(2 ,end=" ")
    if ord(a[i]) >= ord("d") and ord(a[i])<=ord("f"):
        print(3 ,end=" ")
    if ord(a[i]) >= ord("g") and ord(a[i])<=ord("i"):
        print(4 ,end=" ")
    if ord(a[i]) >= ord("j") and ord(a[i])<=ord("l"):
        print(5 ,end=" ")

    if ord(a[i]) >= ord("m") and ord(a[i])<=ord("o"):
        print(6 ,end=" ")
    if ord(a[i] )>= ord("p") and ord(a[i])<=ord("s"):
        print(7 ,end=" ")

    if ord(a[i]) >= ord("t") and ord(a[i])<=ord("v"):
        print(8 ,end=" ")
    if ord(a[i]) >= ord("w") and ord(a[i])<=ord("z"):
        print(9 ,end=" ")

a  = 10
s = str(a)
# li = list(a)
# for i in range(len(li)):

print(s[:])