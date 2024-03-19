def RotateArray(nums,k):
    n = len(nums)
    nums2 =  [0]*n
    nums2[:k] = nums[n-k:]
    nums2[k:] = nums[:n-k]

    return nums2

nums = [1,2,3,4,5,6,7]
k = 3

print(RotateArray(nums,k))