def subset_sum(a,index,n,sum,output):

    if(index==n):
        output.append(sum)
        return

    #ignore
    subset_sum(a,index+1,n,sum,output)
    sum+=a[index]
    subset_sum(a,index+1,n,sum,output)

    return output


a = [3,4,5]
output = []
temp = []
print(subset_sum(a,0,3,sum=0,output=[]))
