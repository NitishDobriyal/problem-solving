def RotateArray(nums,k):
    diff=k
    n = len(nums)
    
    nums2 =  [0]*n
    nums2[:k] = nums[n-k:]
    nums2[k:] = nums[:n-k]
    return nums2

# nums = [1,2,3,4,5,6,7,8,9]
nums = [3,1,6,2,7,4,9,35]
k = 3
#op = [7,8,9,1,2,3,4,5,6]

print(RotateArray(nums,k))