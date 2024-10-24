arr=[8,2,7,5,4,1,9,10]
#op=[9,7,9,9,9,9,10,-1]
res = [-1]*len(arr)
stack=[]
for i in range(len(arr)-1,-1,-1):
    while stack and stack[-1]<arr[i]:
        stack.pop()
    if(stack):
        res[i]=stack[-1]
    stack.append(arr[i])    
print(res)   

'''

Same as Prev GT, isme bas iterate piche se karna
stack me current element dalo
fr cur_ele se stack top cmpare kro, agr stack[top]>cur. To stack[top] is next greater
other wise, while loop lagake stack se pop krte rho, jab tk stack[top] chota hai cur_ele se

'''
