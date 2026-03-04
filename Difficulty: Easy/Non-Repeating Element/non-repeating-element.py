#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key,value in freq.items():
            if value==1:
                return key
        return 0
