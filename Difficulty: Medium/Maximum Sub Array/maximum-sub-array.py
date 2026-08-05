class Solution:
    # Function to find the subarray with the maximum sum
    def findSubarray(self, arr):
    	# code here
    	maxi=-1
    	curr_sum=0
    	
    	start=0
    	ansStart=-1
    	ansEnd=-1
    	
    	for i in range(len(arr)):
    	    
    	    if arr[i]>=0:
    	        curr_sum+=arr[i]
    	        
    	        if (curr_sum>maxi or (curr_sum==maxi and i-start>ansEnd-ansStart)):
    	            maxi=curr_sum
    	            ansStart=start
    	            ansEnd=i
    	    else:
    	        curr_sum=0
    	        start=i+1
    	 
        if ansStart==-1:
            return [-1]
        return arr[ansStart:ansEnd+1]