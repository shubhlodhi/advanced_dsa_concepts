def longest_sub_string(a,n):
    result =0
    for i in range(0,n):
        res =0
        for j in range(i+1,n):
            if a[i] != a[j]:
                res+=1
                result = max(res , result)

            else:
                break

    return result

a = "pwwkew"
n = len(a)
print(longest_sub_string(a,n))

            