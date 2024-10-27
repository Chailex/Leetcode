class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            temp = haystack[i:i+len(needle)]
            print(temp)
            if temp == needle:
                return i
        return -1
