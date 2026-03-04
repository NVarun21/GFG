class Solution:
    def findSum(self, s):
        num = ""
        total = 0
        for char in s:
            if char.isdigit():
                num += char
            else:
                if num:
                    total += int(num)
                    num = ""
        if num:
            total += int(num)
        return total