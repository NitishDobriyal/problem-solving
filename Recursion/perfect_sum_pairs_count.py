def perfect_sum(a,index,n,sum):
    if(index==n):
        return sum==0
    return perfect_sum(a,index+1,n,sum)+perfect_sum(a,index+1,n,sum-a[index])

a = [5,5,0,3,2]
sum = 10

print(perfect_sum(a,0,len(a),sum))

'''Intuition:
Same as target sum, just that we are adding both side recursive tree output
As we can have 0 in our array, so we can't return just by looking when sum==0 return True
Because in that case we will miss [5,5,0] this last 0 as execution got returned
So what we do is we traverse till last, and see if sum==0 then return True else return False

iska mtlb, agr 5,5,0,0,0.. kitne v 0 hon, to v last condition pe to sum 0 hi rahega

Tip: Draw a tree and u'll understand   
'''