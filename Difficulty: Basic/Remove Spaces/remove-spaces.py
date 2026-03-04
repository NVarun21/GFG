#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        res=""
        for char in s:
            if char!=' ':
                res+=char
        return res