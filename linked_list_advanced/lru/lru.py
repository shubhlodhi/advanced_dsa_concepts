from collections import deque
def set_function_in_cache(Q , cap):
    

    dictionary = dict()
    c = 0
    DQ = deque()
    for i in range((Q)):
        key = input("enter key")
        value= str(input("enter the quesries"))


    if   c <= cap:
        DQ.append(key)
        dictionary[key] = value
        c+=1
    if c > cap:
        if key in dictionary:
            del dictionary[key]
        DQ.popleft()
        

        DQ.append(key)
        dictionary[key] = value
    return DQ


# set_function_in_cache(1 ,"a" , 1)
# set_function_in_cache(2 , "b" , 2)
print(set_function_in_cache(6,2))


    

    


