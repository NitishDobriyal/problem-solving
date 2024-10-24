#check if s2 is a subsequence of s1

'''
Example
s1= abcd s2=ad
so a and d comes in the order how it is in s1, so it is a subsequence
'''

s1 = 'abcde'
s2 = 'aeb'
#op-->true

p = 0
q = 0
match = 0
while(p<len(s1) and q<len(s2)):
    if(s1[p]==s2[q]):
        p+=1
        q+=1
        match+=1
    else:
        p+=1
if(match == len(s2)):
    print('True')
else:
    print('False')    


