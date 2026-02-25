class Solution:
    def leaders(self, arr):
        # code here
        leader=[]
        max_right=arr[len(arr)-1]
        leader.append(max_right)
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=max_right:
                max_right=arr[i]
                leader.append(max_right)
        return leader[::-1]