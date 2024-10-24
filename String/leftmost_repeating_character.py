'''
def leftmost_repeating_char(s):
    char = 256
    res = [0]*char
    for i in range(len(s)):
        res[ord(s[i])]+=1
    for i in range(len(s)):
        if(res[ord(s[i])])>1:
            return i
    return -1


'''

#op->b (as it is first char to be repeating)

'''
Approach:
make a 256 sized, character array of ascii.
iterate over string and increase count of values in array.
iterate and check where first time value>1. return it
'''
############ More optimised
def optimised_soln(s):
    char = 256
    op = 1000
    res = [False]*256
    print(res)
    for i in range(len(s)-1,-1,-1):
        if(res[ord(s[i])]==True):
            op = i
        else:
            res[ord(s[i])]=True
    return op

s = 'abdcccb'
# print(leftmost_repeating_char(s))
print(optimised_soln(s))

