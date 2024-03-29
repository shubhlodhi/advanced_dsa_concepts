def calculate_sum_string(a):
    sum  =0
    prec ="0"
    for x in a:
        if x.isdigit():
            prec+=x

            
        else:
            sum+=int(prec)
        # sum+=int(prec)
            prec = "0" 
    return int(prec)

        

a = "1wsa23"
print(calculate_sum_string(a))

        
