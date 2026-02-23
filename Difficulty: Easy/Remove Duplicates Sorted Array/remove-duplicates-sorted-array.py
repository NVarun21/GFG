class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0:
            return arr
        
        i = 0
        
        for j in range(1, n):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        
        return arr[:i+1]   # ✅ return array, not length