
def subsequence(a,index,end,temp,output_list):
    if(index==end):
        output_list.append(temp.copy())
        return 

    subsequence(a,index+1,end,temp,output_list)
    temp.append(a[index])
    subsequence(a,index+1,end,temp,output_list)
    temp.pop() 
    

a = [1,2,3]
output_list = []
temp = []
subsequence(a, 0, len(a), temp, output_list)
print(output_list)

# def subsequence(a, index, end, temp, output_list):
#     if index == end:
#         output_list.append(temp)
#         return

#     # Exclude the current element and move to the next
#     subsequence(a, index + 1, end, temp, output_list)

#     # Include the current element and move to the next
#     subsequence(a, index + 1, end, temp + [a[index]], output_list)

# a = [1, 2, 3]
# output_list = []
# temp = []
# subsequence(a, 0, len(a), temp, output_list)

# print(output_list)
