#User function Template for python3
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        items=[(val[i]/wt[i],val[i],wt[i]) for i in range(len(val))]
        items.sort(reverse=True,key=lambda x:x[0])
        
        total_value=0
        for ratio,value,weight in items:
            if capacity>=weight:
                capacity-=weight
                total_value+=value
            else:
                total_value+=ratio*capacity
                break
        return total_value

        
        

#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends