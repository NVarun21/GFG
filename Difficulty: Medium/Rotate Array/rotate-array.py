class Solution:
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d=d%n
        def rotate(l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        
        rotate(0,d-1)
        rotate(d,n-1)
        rotate(0,n-1)
        return arr