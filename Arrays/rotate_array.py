#Inplace
def reverse(arr,i,j):
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i] 
        i+=1
        j-=1
    return arr    

def rotate_arr(arr,k):
    size = len(arr)
    arr = reverse(arr,i=0,j=size-1)

    #now reverse 2 sub arrays, [7, 6, 5, 4, 3]  and [2, 1]

    arr = reverse(arr,i=0,j=size-k-1)
    arr = reverse(arr,i=size-k,j=size-1)
    
    return arr

arr = [1,2,3,4,5,6,7]
print(rotate_arr(arr,2))

'''Analogy 
orig = 1,2,3,4,5,6,7
1. Reverse the array 

7,6,5,4,3,2,1

2. Again now reverse them from the asked index from where we have to rotate

3,4,5,6,7 and 1,2

'''         