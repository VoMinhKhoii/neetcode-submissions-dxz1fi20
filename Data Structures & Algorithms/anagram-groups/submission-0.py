import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Assumption fix: use defaultdict so that missing keys 
        # automatically initialize to an empty list [].
        dict = defaultdict(list)
        
        def charFreq(s: str) -> dict:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')]+=1
            return tuple(count)
        
        for i in strs:
            signature = charFreq(i)
            dict[signature].append(i)
        
        return list(dict.values())
            


        