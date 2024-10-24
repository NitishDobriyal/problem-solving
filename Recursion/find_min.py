def find_min(arr,min,n):
    if(arr[n]<min):
        min = arr[n]
    if(n<0):
        return min
    return find_min(arr,min,n-1)
arr=[7,2,4,3,6]
print(find_min(arr,arr[len(arr)-1],4))
