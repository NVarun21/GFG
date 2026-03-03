class Solution:
    def findMedian(self, arr):
        #code here.
        n=len(arr)
        arr.sort()
        if n%2!=0:
            return arr[n//2]
        return (arr[n//2-1]+arr[n//2])/2