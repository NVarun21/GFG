class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        Sum=0
        maxi=arr[0]
        for num in arr:
            Sum+=num
            if Sum>maxi:
                maxi=Sum
            if Sum<0:
                Sum=0
        return maxi