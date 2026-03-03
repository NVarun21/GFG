#User function Template for python3
class Solution:

	def equilibrium(self,arr): 
    	# code here
    	total_sum=sum(arr)
    	left_sum=0
    	for i in range(len(arr)):
    	    right_sum=total_sum-left_sum-arr[i]
    	    if left_sum==right_sum:
    	        return "true"
    	    left_sum+=arr[i]
    	return "false"