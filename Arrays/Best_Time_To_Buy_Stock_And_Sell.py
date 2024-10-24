a=[2,3,10,6,4,8]

#O(n) approach
min=0
max_diff=0
for i in range(1,len(a)):
    if(a[i]>a[min]):
        max_diff = max(max_diff,a[i]-a[min])
    else:
        min=i
print(max_diff) 
#So to get max profit one should've bought stock at price 2 and sold at 10,           

# TC-O(n^2)
# max_diff=0
# for i in range(len(a)-1):
#     j=i+1
#     while(j<len(a)):
#         if(a[j]>a[i] and a[j]-a[i]>max_diff):
#             max_diff=a[j]-a[i]
#         j+=1    
# print(max_diff)     

           