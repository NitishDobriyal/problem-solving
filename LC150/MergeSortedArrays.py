
def MergeSortedArrays(nums1,nums2,m,n):
    last=len(nums1)-1
    p=m-1
    for i in range(n-1,-1,-1):
        if(p==-1):
            break
        while(p!=-1):           
            if(nums1[p]>nums2[i]):
                nums1[last],nums1[p]=nums1[p],nums1[last]
                last-=1
                p-=1
            else:
                nums1[last]=nums2[i]    
                last-=1
                break
    for i in range(m):
        if(nums1[i]==0):
            nums1[i]=nums2[i]
        else:
            break 
    return nums1    

nums1 = [1,8,9,0,0,0]
m = 3
# nums2 = [2,3,5]
nums2 = [1,2,17]
n = 3

print(MergeSortedArrays(nums1,nums2,m,n))

#Intuition
'''
1. Last element of nums1 and nums2 are the greatest,so we will compare elements from end and which ever 
is greater will put that in nums1 end, where we have zeroes.
2. So loop nums2, from end till -1 index and if at any time, nums1 is fully compared, just return
3. Now nums1 will be fixed, and we have to loop nums2 and put elements in nums1 where we have 0(zeroes)
'''
  
