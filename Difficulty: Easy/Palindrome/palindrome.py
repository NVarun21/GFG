class Solution:
    def isPalindrome(self, n):
		# code here
		revnum=0
		temp=n
		while n>0:
		    digit=n%10
		    revnum=revnum*10+digit
		    n=n//10
		return temp==revnum