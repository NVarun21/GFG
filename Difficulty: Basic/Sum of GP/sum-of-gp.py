class Solution:
    def sum_of_gp(self, n, a, r):
        if r == 1:
            return a * n
        return a * (r**n - 1) // (r - 1)