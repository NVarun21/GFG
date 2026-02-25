class Solution:
    def maxConsecBits(self, arr):
        maxcount = 0
        count0 = 0
        count1 = 0
        
        for num in arr:
            if num == 0:
                count0 += 1
                count1 = 0
            else:
                count1 += 1
                count0 = 0
            
            maxcount = max(maxcount, count0, count1)
        
        return maxcount