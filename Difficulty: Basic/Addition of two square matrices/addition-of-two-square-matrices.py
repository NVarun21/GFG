#User function Template for python3

class Solution:
	def Addition(self, matrixA, matrixB):
		# Code here
		n=len(matrixA)
		for i in range(n):
		    for j in range(n):
		        matrixA[i][j]+=matrixB[i][j]
		return matrixA