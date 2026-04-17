class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        nsum=(n*(n+1))//2
        Sum=sum(arr)
        return nsum-Sum