# def merge_sort(a,n):
#     mid = n//2
#     low = 0
#     high = n
#     left_array = a[low:mid]
#     right_array = a[mid:high]

#     i =0
#     j =0
#     k =0

#     res =[]
#     while i<=len(left_array) and j<=len(right_array):
#         # if a[low] < a[high]:
#         if left_array[i] <= right_array[j]:
#             res.append(left_array[i])
#             i+=1



#         else:
#             res.append(right_array[j])
#             j+=1

#     while i<n:
#         res.append(left_array[i])
#         i+=1

#     while j<n:
#         res.append(right_array[j])
#         j+=1

#     for i in range(len(res)):
#         print(res[i] ,end="")

#     return res
# def merge_ll(head):
    
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def print_list(a):
    for i in range(len(a)):
        print(a[i] ,end=" ")


a  = [13,12,14,34,53]
n = len(a)
mergeSort(a)
print_list(a)

# mid = n//2
# low = 0
# high = n
# left_array = a[low:mid]
# right = a[mid:high]
# print(left_array)
# print(right)

