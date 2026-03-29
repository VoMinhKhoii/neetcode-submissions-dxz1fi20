import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def charFrequency(s: str) -> dict:
            alpha_dict = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
            for i in range(len(s)):
                if alpha_dict.get(s[i], 0) == 0:
                    alpha_dict[s[i]] = 1
                else:
                    alpha_dict[s[i]] = alpha_dict.get(s[i], 0) + 1
            return alpha_dict
        
        if charFrequency(s) != charFrequency(t):
            return False
        return True
        