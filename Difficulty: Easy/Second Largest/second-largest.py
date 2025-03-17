#User function Template for python3
class Solution:
    def largest(self,arr):
        largest=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        return largest
    def getSecondLargest(self, arr):
        # Code Here
        secondlargest=-1
        largest=self.largest(arr)
        for i in range(len(arr)):
            if  arr[i]>secondlargest and arr[i]!=largest:
                secondlargest=arr[i]
        return secondlargest
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends