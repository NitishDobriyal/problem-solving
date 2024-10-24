def target_sum(a,index,n,sum):
    if(sum==0):
        return True
    if(index==n or sum<0):
        return False
    return target_sum(a,index+1,n,sum) or target_sum(a,index+1,n,sum-a[index])

a = [5,6,2,7,0]
sum = 10

print(target_sum(a,0,len(a),sum))

'''
Intuition:
Simple, hmare pass array hai recursive way me ek bar index ko ignore kro, ek bar consider kro.
And consider k time pe, sum se utna minus kardo like sum-a[index]
jab sum 0 hojae mtlb answer agaya
'''
