#User function Template for python3
class Solution:
	def removeDuplicates(self, s):
	    # code here
	    res=""
	    for ch in s:
	        if ch not in res:
	            res+=ch
	    return res