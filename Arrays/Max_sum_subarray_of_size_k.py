# O(n) solution in Python3 for finding 
# maximum sum of a subarray of size k

# Returns maximum sum in
# a subarray of size k.
def maxSum(arr, n, k):

	# k must be smaller than n
	if (n < k):
	
		print("Invalid")
		return -1
	
	# Compute sum of first
	# window of size k
	res = 0
	for i in range(k):
		res += arr[i]

	# Compute sums of remaining windows by
	# removing first element of previous
	# window and adding last element of 
	# current window.
	print('RES',res)
	curr_sum = res
	for i in range(k, n):
        
		curr_sum += arr[i] - arr[i-k]
		res = max(res, curr_sum)
		print('I=',i)
		print('i-k',i-k)

	return res

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

