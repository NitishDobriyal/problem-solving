def display(arr,n):
    if(n==0):
        return
    # display(arr,n-1)
    print(arr[n-1])
    display(arr,n-1)

display([1,4,5,3,9,7,2,8,6],9)
