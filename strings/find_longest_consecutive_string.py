def cobsecutive_sub_string(a,n):
    dict1 = dict()
    final_result =0
    result =0
    i =0
    while i<n:
        # element = a[i]
        if a[i] not in dict1:
            value = a[i]
            result +=1
            dict1[value] =1
            final_result = max(result , final_result)
            i+=1

        if  a[i] in dict:
            result =0
            dict2 = dict()
            for j in range(i,n):
                new_value = a[j]
                if new_value not  in dict2:
                    dict2[new_value] =1
                    result+=1
                    final_result = max(result ,final_result)

                if new_value in dict2:
                    break
                
        i+=1
    return final_result


a = "pwwkew"
n = len(a)
print(cobsecutive_sub_string(a,n))

