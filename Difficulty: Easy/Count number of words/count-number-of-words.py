class Solution:
    def countWords(self, s):
        s = s.replace('\\n', ' ').replace('\\t', ' ')
        k = s.split()
        return len(k)