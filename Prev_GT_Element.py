a=[8,2,7,5,4,1,9,10]
#op=[-1,8,8,7,5,4,-1,9]
res = [-1]*len(a)
stack=[]
for i in range(len(a)):
    while stack and stack[-1]<a[i]:
        stack.pop()
    if(stack):
        res[i]=stack[-1]
    stack.append(a[i])    
print(res)        


