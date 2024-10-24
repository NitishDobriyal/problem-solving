def perfect_sum_repitition(a,index,n,target):
    if(index==n):
        return target==0
    if(target<0):
        return False
    
    return perfect_sum_repitition(a,index+1,n,target)+perfect_sum_repitition(a,index,n,target-a[index])

a = [2,3,4]

print(perfect_sum_repitition(a,0,len(a),target=6))