/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution {
    longestSubarray(arr, k) {
        // code here
        let prefix={};
        let maxLen=0;
        let sum=0;
        for(let i=0;i<arr.length;i++){
            sum+=arr[i];
            if(sum==k){
                maxLen=i+1;
            }
            
            let required=sum-k;
            if(required in prefix){
                maxLen=Math.max(maxLen,i-prefix[required]);
            }
            
            if(!(sum in prefix)){
                prefix[sum]=i;
            }
        }
        return maxLen;
    }
}
