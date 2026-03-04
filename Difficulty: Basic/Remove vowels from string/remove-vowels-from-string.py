# User function Template for python3
class Solution:
    def removeVowels(self, s):
        vowels = "aeiouAEIOU"
        result = ""
        
        for ch in s:
            if ch not in vowels:
                result += ch
                
        return result