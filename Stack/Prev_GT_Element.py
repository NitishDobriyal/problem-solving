a=[8,2,7,5,4,1,9,10]
#op=[-1,8,8,7,5,4,-1,-1]
res = [-1]*len(a)
stack=[]
for i in range(len(a)):
    while stack and stack[-1]<a[i]:
        stack.pop()
    if(stack):
        res[i]=stack[-1]
    stack.append(a[i])    
print(res)   

'''
Approach:
ek stack lelo
ek res array, initialise every element with -1

iterate over input arr, check kro kya current element, stack ke top se bada hai
agr hai to pop krte jao jab tk stack[top] becomes greater. iska mtlb current element 
se bada element mil gaya. 

SIMPLE bro
'''
