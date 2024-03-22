from collections import deque

def BestTime(prices):
    #O(n) time and O(1) space
    profit = 0
    for i in range(1,len(prices)):
        if(prices[i]>prices[i-1]):
                profit+=prices[i]-prices[i-1]
    return profit
    

# prices = [7,1,5,3,4,6]
prices = [6,1,3,2,4,9]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
print(BestTime(prices))
'''
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''

'''
Intuition: Simple just buy on the day when prices was more than previous day and add profit.
'''