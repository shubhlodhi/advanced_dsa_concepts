def kmp_find_algo(str , pattern):
    str_len = len(str)
    pat_len = len(pattern)
    f =0
    for i in range(0,str_len-pat_len+1):
        j =0
        
        # for j in range(pat_len):
        while j<pat_len:
            if str[i+j] != pat[j]:
                break

            j+=1

            if j == pat_len:
             return i



        # for j in range(pat_len):
            
        #     if str[i+j] == pattern[j]:
        #         f+=1
        #         if f == pat_len:
        #             return i
                

str = "abcdef"
pat = "bcd"
print(kmp_find_algo(str,pat))

#  using kmp algorothm



