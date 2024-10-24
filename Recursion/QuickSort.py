
def partition(arr,start,end):
    pos = start
    for i in range(start,end+1):
        if(arr[i]<=arr[end]):
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return pos-1

def quickSort(arr,start,end):
    if(start>=end):
        return
    pivot = partition(arr,start,end)
    quickSort(arr,start,pivot-1)
    quickSort(arr,pivot,end)

arr = [6,4,5,2,1,3]
quickSort(arr,start=0,end=5)
print(arr)



'''
 TC: O(logn) avg-- 
     O(n^2) worst, when arr is already sorted

 SC: O(log n) avg
     O(n) worst
'''

