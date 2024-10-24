
# def permutation(a,size,visited,temp,final):

#     if(len(temp)==size):
#         # print(temp)
#         final.append(temp.copy())
#         return

#     for i in range(size):
#         if(visited[i]==0):
#             visited[i]=1
#             temp.append(a[i])
            
#             permutation(a,size,visited,temp,final)
#             visited[i]=0
#             temp.pop(-1)
#     return final

# def permutation(a, size, visited, temp, final):
#     if len(temp) == size:
#         final.append(temp)  # No need for a copy here as we create new lists
#         return

#     for i in range(size):
#         if visited[i] == 0:
#             visited[i] = 1
#             permutation(a, size, visited, temp + [a[i]], final)  # Create new list by adding a[i]
#             visited[i] = 0

#     return final

def permutations_optimised(a,index,size,final):
    if(index==size):
        final.append(a.copy())
        return


    for i in range(index, size):
        a[i],a[index] = a[index],a[i]
        permutations_optimised(a,index+1,size,final)
        a[index],a[i] =  a[i],a[index]

    return final

a = [1,2,3]
# visited = [0,0,0]
# temp = []
final = []
# print(permutation(a,len(a),visited,temp,final))

print(permutations_optimised(a,0,len(a),final))
# print(final)