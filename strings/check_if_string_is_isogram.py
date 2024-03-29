def string_is_isogram(a):
    dict1 = dict()
    for i in range(0,len(a)):
        if a[i] not in dict1:
            dict1[a[i]]  = 1

        else:
            return False
        
    return True


a = "abcdefghi"
print(string_is_isogram(a))