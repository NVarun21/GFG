class Solution:
    def toggleCase(self, s):
        # code here
        res=""
        for i in range(len(s)):
            if s[i].islower():
                res+=s[i].upper()
            else:
                res+=s[i].lower()
        return res
