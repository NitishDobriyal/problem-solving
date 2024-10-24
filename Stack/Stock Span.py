class Solution:
    
    #Function to calculate the span of stock price for all n days.
    def calculateSpan(self,a,n): #Optimized solution
        #code here
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and (a[stack[-1]]<=a[i]):
                stack.pop()
            if not stack:
                res[i]=i+1
            else:
                res[i]=i-stack[-1]
            stack.append(i)   
        return res
        
   #def calculateSpan(self,a,n):   #N^2 complexity 
        
        # res=[0]*n
        # for i in range(n-1,-1,-1):
        #     count=1
        #     for j in range(i-1,-1,-1):
        #         if(a[i]>a[j]):
        #             count+=1
        #         else:
        #             break
        #     res[i]=count
        # return res