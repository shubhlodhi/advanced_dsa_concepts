import math
def index_minimum_char(p,p1):
    final_result = math.inf
    for i in range(0,len(p1)):
        for j in range(len(p)):
            if p1[i] == p[j]:
                res = i
                final_result = min(res, final_result)
                final_value = p1[i]

    return final_value
    # return final_result

a = "zsyle"
p = "ys"
print(index_minimum_char(a,p))

    
