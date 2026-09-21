class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq={}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        
        for key,value in freq.items():
            if value==1:
                return key
        return -1