s = 'aabbxtxbbaa'

p = 0
q = len(s)-1

c=0
while(p<q and s[p]==s[q]):
    c+=1
    p+=1
    q-=1


if(c==len(s)//2):
    print('True')
else:
    print('False')    


'''
Approach:

two ptrs from left and right, loop till p<q and s[p]==s[q]
increment counter for every match

compare count with half length os orig string, if equal, then TRUE
'''


