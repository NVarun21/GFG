class Solution:
    def leaders(self, arr):
        # code here
        ans=[]
        n=len(arr)
        maxi=arr[n-1]
        ans.append(maxi)
        for i in range(n-2,-1,-1):
            if arr[i]>=maxi:
                ans.append(arr[i])
                maxi=arr[i]
        ans.reverse()
        return ans