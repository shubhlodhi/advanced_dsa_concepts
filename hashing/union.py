def union(a,b,c,na , nb , nc):
    dictionary = dict()
    i =0
    union = (a+b+c)
    n_all = (na+nb+nc)

    while i<n_all:
        element = union[i]
        if element in dictionary:
            dictionary[element] +=1
            # i+=1
        if element not in dictionary:
            dictionary[element] =1

        i+=1

    return len(dictionary)

# a =[5,3]
# b = [1,2,3,4,5]
# c =[1,2,3]
a =[6 ,2] 
b = [85, 25, 1, 32, 54, 6]
c = [85, 2] 
na = len(a)
nb = len(b)
nc = len(c)
print(union(a,b,c,na,nb,nc))