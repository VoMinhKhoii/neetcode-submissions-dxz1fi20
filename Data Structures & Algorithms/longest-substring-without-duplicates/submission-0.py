class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0,0
        maxLen = 0
        currLen = 0
        freq = defaultdict()
        while end < len(s):
            if freq.get(s[end], 0) != 0:
                freq[s[start]] = freq[s[start]] - 1
                start += 1
                currLen -= 1
            else:
                freq[s[end]] = 1
                currLen += 1
                maxLen = max(maxLen, currLen)
                end += 1
        return maxLen
        






        