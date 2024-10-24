
def longest_sub_without_repeating_chars(s):
    start,end,i,j = 0,len(s)-1,0,0
    map = {}
    max_size = 0
    while(j<len(s)):
        if((s[j] not in map) or (map[s[j]]<i)):
            map[s[j]]=j
        else:
            i=map[s[j]]+1
            map[s[j]]=j
        if((j-i+1)>max_size):
            start = i
            end = j
            max_size = j-i+1
        j+=1
    return s[start:end+1]

# s = '01134127232145244637248458'
s = 'addasdaf'
# s = 'abcd'
#op = 'wke'

print(longest_sub_without_repeating_chars(s))