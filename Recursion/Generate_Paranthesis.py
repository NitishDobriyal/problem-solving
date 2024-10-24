def generate(s,n,temp, left,right):
    if(left>n):
        return
    elif(right>left):
        return
    elif((left==right) and left==n):
        temp.append(s)
        return
    generate(s+'(',n,temp, left+1,right)  
    generate(s+')',n,temp, left,right+1)  

s = '('
temp = []
generate(s,3,temp,left=1,right=0)
print(temp)