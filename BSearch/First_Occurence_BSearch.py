import math
a=[4,11,12,15,17,19,19,19,19,25]
n=len(a)
#Find first occ of 19, i.e 5 should be ouptut
def FirstOccurrence(a,k):
    l=0
    r=n-1 
    while(l<=r):
        mid = math.floor(l+(r-l)/2)
        if(a[mid]==k):
            if(mid-1>0 and a[mid-1]==k):
                r=mid-1
            else:
                return mid    
        elif(k<a[mid]):
            r=mid-1
        else:
            l=mid+1
    return False

print(FirstOccurrence(a,19))                    


