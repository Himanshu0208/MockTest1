class Solution:
    def firstUniqChar(self, s: str) -> int:
        hset = collections.Counter(s)
        for index in range(len(s)):
            if(hset[s[index]] == 1):
                return index
        return -1
