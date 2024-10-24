a = [1, 2, -1, 3, -4 ,-4, 5, -2, 7, -5, -6, 8]
k=3
p = 0
q = k-1
res = []
while(p<=q and q<len(a)):
    if(a[p]<0):
        res.append(a[p])
        print(f'p={p},q={q}')
        q+=1
        p=q-2
        
    else:
        if(p==q):
            res.append(0)
        p+=1
print(res)

