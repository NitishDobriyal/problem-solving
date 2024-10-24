def containsDuplicate(nums):
        #Time O(nlogn) O(1) space
        '''
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                return True
        '''
        
        #O(n) time, O(n) space
        u_set = set()
        for i in nums:
            if i not in u_set:
                u_set.add(i)
            else:
                return True
        return False 
         

nums = [1,2,3,4,5,2]
print(containsDuplicate(nums))