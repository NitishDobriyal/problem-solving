
def getCountOFAnagram(s,pattern):
    n=len(s)
    p=0
    q=0
    d=dict()
    ans=0
    k=len(pattern)
    for i in pattern:
        d[i]=d.get(i,0)+1
    count=len(d)
    while q<n:
        if s[q] in d:
            d[s[q]]-=1
            if d[s[q]] == 0:
                count-=1
        if q-p+1 <k: # window size limit
            q+=1
        elif q-p+1 == k:
            if count==0:
                ans+=1
            if s[p] in d :
                d[s[p]]+=1
                if d[s[p]] == 1:
                    count+=1
            p+=1
            q+=1
    return ans

s = "baaabbaabaab"
pattern = "aaba"

print(getCountOFAnagram(s,pattern))


# while(q<len(s)):
#     #check if cur ele is in map and also if it is greater than 0, if so then decrement its value in map
#     print(f'cur ele {s[q]}')
#     if s[q] in map:
#         if(map[s[q]]>0):
#             map[s[q]]-=1
#             if(map[s[q]]==0):
#                 count-=1
#     print(f'count = {count}')
#     if(q >= len(k)-1):
#         print('K size breached')
#         if(count==0):
#             ans+=1
#         if s[p] in map:
#             map[s[p]]+=1
#             if(map[s[p]]==1):
#                 count+=1    
#         print(map)
#         print(f'count={count}')
#         p+=1
#     q+=1
      
#     print(f'ans = {ans}')
#     print('-------------')
# print(ans)
            

