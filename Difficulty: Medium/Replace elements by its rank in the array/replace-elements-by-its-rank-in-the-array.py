#User function Template for python3

class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        sorted_arr=sorted(arr)
        rank={}
        current_rank=1
        for num in sorted_arr:
            if num not in rank:
                rank[num]=current_rank
                current_rank+=1
        return [rank[num] for num in arr]