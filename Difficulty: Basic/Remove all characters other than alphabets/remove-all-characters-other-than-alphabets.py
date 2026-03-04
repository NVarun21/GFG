# User function Template for python3

class Solution:
    def removeSpecialCharacter(self, S):
        res = []
        
        for char in S:
            if char.isalpha():
                res.append(char)
        
        if not res:
            return "-1"
            
        return ''.join(res)