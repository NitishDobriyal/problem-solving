import math
a=[1,2,4,5,6,7,8]
#search any number and it's position in an array
n=len(a)
def BinarySearch(a,k):
    l=0
    r=n-1
    
    while(l<=r):
        mid = math.floor(l+(r-l)/2)
        if(a[mid]==k):
            return mid
        elif(k<a[mid]):
            r=mid-1
        else:
            l=mid+1    
    return False

print(BinarySearch(a,1))       