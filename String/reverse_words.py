s = 'welcome to gfg'

def reverse_words(s):
    l = s.split(' ')
    res = ''
    for i in l[::-1]:
        res+=i+' '
    return res.rstrip()

print(reverse_words(s))
    

'''
Approach:
iterate keep track of beginning and end of one word using space tracker.

then reverse individual words.
At last then reverse last word and then reverse whole string.

'''
