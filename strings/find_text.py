def find_text(string,pattern):
    for i in range(0,len(string)):
        # pattern_index = 0
        pattern_index =0
        for j in range(i,len(string)):
            
            if pattern_index == len(pattern)-1:
                print(i)
            # pattern_index =0
            if pattern_index>=len(pattern):

                 pattern_index =0

                #  break
            if string[j] != pattern[pattern_index]:
                break
            if string[j] == pattern[pattern_index]:
                pattern_index+=1
                # a = int(set(i))
                # print(i)


    # return a
            # else:
            # else:
                #  print(i)
        # print(i)        # print(i)
                # 

                
                   
                    # pattern
            # print(i)

a ="ABABABCD"
pattern = "ABAB"
print(find_text(a,pattern))