def nth_prime_digit(n):
    i =0
    n1 = n*n 
    value = 2
    while i<n:
     
     for j in range(value,n1):
            if j<10:
              if j %2 != 0:
                print(j , end=" ")
                i+=1
                value =j
                break
              # j = j
                # break
                # print(i)

            if j>=10:
               string = str(j)
               for i in range(len(string)):

                  if int(string[i]) == 1:
                     break
                  if int(string[i]) % 2 ==0:
                    break
                      
               
                   
               else:
                 print(string ,end=" ")
                 i+=1
    # i+=1          


n =10
nth_prime_digit(n)
# num = ""

def primes(n):
   a1 = []
   a1.append(2)
   a1.append(3)
  #  rank =10
   for i in range(3,n):
      # print(2)

      if i % 2  == 0 or i%3==0:
        continue
        #  a1.append(i)
        #  print(i,end=" ")
      else:
         print(a1.append(i))
      # rank -=1
  #  f =[]
   for i in range(0,len(a1)):
    # curr = 2
    # if rank == 0:
     
     for j in range(0,len(a1)):
       a1.append(a1[i]*10+a1[j]) 
       
      #  if f == 11:
          # continue
      #  print(f ,end=" ")

      #  rank-=1
  #  return a1
   for i in range(0,n):
      if i == n-1:
         return a1[i]    
a =10
# n =len(a)
print(primes(a))

def prime_new(a):
   n = [True]*a
   n[1] = False
  #  for i in range(3,n):
    # if i % 2 == 0 and i%3==0:
      #  n[i] = False


   return n

a = 10
print(prime_new(a))





