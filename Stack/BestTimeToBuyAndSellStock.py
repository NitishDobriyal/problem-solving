from collections import deque

def BestTime(prices):

    '''
    O(n) time and O(1) space
    '''
    if(len(prices)==1):
        return 0
    min_ele = prices[0]
    max_diff = 0
    for price in prices:
        min_ele = min(min_ele,price)
        max_diff = max(max_diff,price-min_ele)
    return max_diff    


    '''
    O(n) time O(n) space
    '''
    # stack = deque()
    # max_diff=0
    # for i in range(len(prices)-1,-1,-1):
    #     if(stack):
    #         if(prices[i]>stack[-1]):
    #             stack.append(prices[i])
    #         else:    
    #             max_diff=max(max_diff,stack[-1]-prices[i])
    #     else:
    #         stack.append(prices[i])        
    # return max_diff       


prices = [4,7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,0,1,0,1]   
# prices = [11] 
print(BestTime(prices))
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

'''
Intuition(Max diff when greater element is after smaller one) - Stack
'''