#User function Template for python3
class Solution:
    def sort(self, s): 
        #code here
        freq=[0]*26
        res=""
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for i in range(26):
            res+=chr(i+97)*freq[i]
        return res