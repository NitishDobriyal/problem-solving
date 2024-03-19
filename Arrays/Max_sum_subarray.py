a=[-2,1,-3,4,-1,2,1,-5,4]
#Kadane's Algo

curr_max = a[0]
max_so_far = a[0]

for i in range(1,len(a)):
    curr_max = max(a[i],curr_max+a[i])
    max_so_far = max(curr_max,max_so_far)

print(max_so_far)