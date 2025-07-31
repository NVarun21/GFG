class Solution:
    def countFreq(self, arr):
        #code here
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        result=[[key,value] for key,value in freq.items()]
        return result