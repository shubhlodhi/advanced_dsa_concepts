def s(txt,pat):
    d = dict()
    for i in range(0,len(pat)):
        string_value = pat[i]
        d[string_value] = i+1

        # j =0
        # for j in range(len(pat)):
    # return d
    sums = sum(d.values())
    # return sums
    # for i in range(0,len(txt)):
        # j =0
        # value =0
    value =0
    for j in range(len(pat)):
            # value = 0
            key = txt[j]
            val = d[key]

            value += val
            
            # if txt[i] == pat[j]:
                # find_element = txt[i]
                # value += d[find_element]
                # if sums == value:
                    # print("yes")
                # break

            # if sums == value:
            #  print("yes")





    
str = "geeksforgeeks"
pat = "frog"
print(s(str,pat))


