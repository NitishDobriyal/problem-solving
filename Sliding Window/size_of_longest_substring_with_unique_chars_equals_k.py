

def length_of_longest_sub(s,k):

    map = {}
    unique_chars = len(map)
    i = 0
    j = 0
    max_size = 0
    while(j<len(s)):
        if(unique_chars<=k):
            if(s[j] in map):
                map[s[j]]+=1
            else:
                map[s[j]]=1
                unique_chars+=1
            if(unique_chars==k):
                max_size = max(max_size,(j-i)+1)
        elif(unique_chars>k):
            while(unique_chars>k):
                map[s[i]]-=1
                if(map[s[i]])==0:
                    unique_chars-=1
                i+=1
        j+=1

    return max_size

s = 'aabacbebebe'
k = 3 #k unique chars

print(length_of_longest_sub(s,k))

'''
Approach:
ek map lelo,i and j 0 se start kro, map me items dalte raho, 
unique_chars = 0 (length of map), starting me 0 hai
max_size of substring = 0
loop j<len(s)

if unique_chars<=k: #mtlb abhi limit tk nhi pahuche
    to elements ko map me dalte jao
    if unique_chars == k:
        to max_size calculate kro, kaise? j-i+1, agar zda hai to update krdo

if unique_chars>k: #mtlb limit se zda agye,
    while lagado :
    ith position pe jo bhi ele hai, uska count reduce kro
    agr wo element 0 hogya, to unique chars ko -1 krdo

last me j+=1 #(j tab hi bdhega jab unique_chars<=k honge)



'''
