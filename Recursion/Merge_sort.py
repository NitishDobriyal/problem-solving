def merge(arr,start,end,mid):
    left = start
    right = mid+1
    temp = []
    while(left<=mid and right<=end):
        if(arr[left]<arr[right]):
            temp.append(arr[left])
            left+=1
        elif(arr[right]<arr[left]):
            temp.append(arr[right])
            right+=1
    # while(left<=mid):
    #     temp.append(arr[left])
    #     left+=1
    # while(right<=end):
    #     temp.append(arr[right])
    #     right+=1
    temp.extend(left[left_index:])
    temp.extend(right_half[right_index:])
    
    return temp

def mergesort(arr, start, end):
    print({start},'and',{end})
    if(start==end):
        
        return
    mid = start + (end-start)/2
    mergesort(arr, start, mid)
    mergesort(arr, mid+1, end)
    return merge(arr,start,end,mid)

arr = [4,2,5,7,12,40,21,8]
print(mergesort(arr,0,7))