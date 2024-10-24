
def sortColors(arr):
    
    #general thinking
    #O(n) time, 2 passes
    '''
    loop through array, count 0s 1s and 2s in variable.
    Then create a new array, and insert 0s,1s,2s
    '''
    zeroes = 0
    ones = 0
    twos = 0
    for i in arr:
        if(i==0):
            zeroes+=1
        elif(i==1):
            ones+=1
        else:
            twos+=1
    
    for i in range(len(arr)):
        if(zeroes!=0):
            # print('yes')
            arr[i]=0
            # print('i=',i)
            zeroes-=1
            continue
        elif(ones!=0):
            arr[i]=1 
            ones-=1
            continue
        else:
            arr[i]=2
            twos-=1
            continue    

    '''
    1 pass thinking
    '''
    


    return arr

arr = [0, 1, 2, 0, 1, 2]
print(sortColors(arr))
# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}