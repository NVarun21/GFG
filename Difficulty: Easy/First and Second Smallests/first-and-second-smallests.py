class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        smallest=float('inf')
        Ssmallest=float('inf')
        for num in arr:
            if num<smallest:
                Ssmallest=smallest
                smallest=num
            elif num<Ssmallest and num!=smallest:
                Ssmallest=num
        if Ssmallest==float('inf'):
            return [-1]
        return [smallest,Ssmallest]
