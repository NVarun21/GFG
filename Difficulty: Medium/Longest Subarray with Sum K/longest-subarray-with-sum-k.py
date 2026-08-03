class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix={}
        maxlen=0
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            
            if s==k:
                maxlen=i+1
                
            if (s-k) in prefix:
                maxlen=max(maxlen,i-prefix[s-k])
            
            if s not in prefix:
                prefix[s]=i
                
        return maxlen