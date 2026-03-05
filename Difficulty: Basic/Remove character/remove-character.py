#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        res=""
        for char in str1:
            if char not in str2:
                res+=char
        return res