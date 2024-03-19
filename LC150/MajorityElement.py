
def majority_ele(nums):
    count = 0
    candidate = 0
    for num in nums:
        if(count==0):
            candidate = num
        if(candidate==num):
            count+=1
        else:
            count-=1
    return candidate                

nums = [2,1,3,1,3,1,1,3,3,1,3,10,3,3]
print(majority_ele(nums))

#Intuition
'''
We assume that first ele is the majority one, if the count becomes zero somewhere,
that means, it is lagging and next element is about to come which can be the potential majority.

Count becoming zero doesn't mean that, that particular ele is not majority.

As we know that there is exactly one ele which is majority element, so eventually that
element will take lead either at start or towards the end.
'''