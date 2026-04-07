class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = [0] * 26
        freqWindowS2 = [0] * 26

        for i in s1:
            idx = ord(i) - ord('a')
            freqS1[idx] += 1

        left, right = 0,0
        while right < len(s2):

            idxRight = ord(s2[right]) - ord('a')
            freqWindowS2[idxRight] += 1

            if freqWindowS2 == freqS1:
                return True

            idxLeft = ord(s2[left]) - ord('a')

            if right < len(s1)-1:
                right += 1
                continue
            else:
                freqWindowS2[idxLeft] -= 1
                left += 1

            right += 1
        return False
            

            
    