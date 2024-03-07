nums=[2,1,5,6,2,3]
a=[]
stack=[]
for i in range(len(nums)):
    while stack and nums[stack[-1]]>nums[i]:
        stack.pop()
    if not stack:
        a.append((i+1)*nums[i])
    else:
        a.append((i-stack[-1])*nums[i])
    stack.append(i)   

stack2=[]    
for i in range(len(nums)-1,-1,-1):
    j=len(nums)-i-1
   
    while stack2 and nums[stack2[-1]]>nums[i]:
        stack2.pop()
    if not stack2:
        a[i]+=(j)*nums[i]
    else:
        a[i]+=(stack2[-1]-i-1)*nums[i]
    stack2.append(i)     

print(max(a))
