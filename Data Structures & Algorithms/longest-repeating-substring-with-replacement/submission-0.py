class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left, right = 0, 0
        # No need to shrink window, we just need to expand
        # And keep track of the largest historical frequency
        # No need to recount maxFreq
        maxFreq = 0
        maxLen = 0
        while right < len(s):
            maxFreq = max(maxFreq, freq[ord(s[right]) - ord('A')])
            if ((right - left) - maxFreq) <= k:
                freq[ord(s[right]) - ord('A')] += 1
                right += 1
                maxLen += 1
            else:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
                maxLen -= 1
        return maxLen
            


        
            
