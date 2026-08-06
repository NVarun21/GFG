class Solution:
    def leaders(self, arr):
        # code here
        rev=[]
        leader=arr[len(arr)-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=leader:
                rev.append(arr[i])
                leader=arr[i]
        rev.reverse()
        return rev