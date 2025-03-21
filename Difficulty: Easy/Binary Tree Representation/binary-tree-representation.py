#User function Template for python3
from collections import deque

class Solution:
    def createTree(self, root, l):
        # Code here
        if not l or len(l)<7:
            return root
        queue=deque([root])
        index=1
        while queue and index<len(l):
            curr=queue.popleft()
            if index<len(l):
                curr.left=Node(l[index])
                queue.append(curr.left)
                index+=1
            if index < len(l):
                curr.right = Node(l[index])
                queue.append(curr.right)
                index += 1
        return root
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def traverseInorder(temp, inorder):
    if(temp!=None):
        traverseInorder(temp.left, inorder)
        inorder.append(temp.data)
        traverseInorder(temp.right, inorder)
    return
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        arr= list(map(int, input().split()))
        root=Node(arr[0])
        root.left=Node(arr[1])
        root.right=Node(arr[2])
        root.left.left=Node(arr[3])
        root.left.right=Node(arr[4])
        root.right.left=Node(arr[5])
        root.right.right=Node(arr[6])
        
        
        obj=Solution()
        root0=Node(arr[0])
        obj.createTree(root0, arr)
        
        a=[]
        traverseInorder(root0, a)
        b=[]
        traverseInorder(root, b)
        
        if(a==b):
            print(1)
        else:
            print(-1)
        print("~")
# } Driver Code Ends