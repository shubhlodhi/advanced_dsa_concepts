
def intersection( nums1, nums2):
        # """
        dictionary = dict()
        for i in range(0,len(nums1)):
            dictionary[nums1[i]]=i
        s =set(nums2)
        for i in range(len(s)):
            # dictionary[nums1[i]]
            if s[i] in dictionary:
                print(s[i])

a =[2,2]
b =[1,2,2,1]
intersection(a,b)
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         # """
#         result = []
#         dictionary = dict()
#         for i in range(0,len(nums1)):
#             dictionary[nums1[i]]=1

#         for i in range(len(nums2)):
#             # dictionary[nums1[i]]
#             if nums2[i] in dictionary:
#                 # print(nums2[i])
#                 result.append(nums2[i])

#         return result
# a =[2,2]
# b =[1,2,2,1]
# # Solution.intersection(a,b)
# a1 = object(a)
# b2 = object(b)
# Solution.intersection(a1,b2)

