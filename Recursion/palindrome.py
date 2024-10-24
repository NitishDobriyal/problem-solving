def pali(s,i,j):
    if(s[i]!=s[j]):
        return False
    if(i>=j):
        return True
    return pali(s,i+1,j-1)

s = 'nampxipman'
i=0
j=len(s)-1
print(pali(s,i,j))