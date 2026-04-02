class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters, strip whitespaces, lowercase, concat
        s = "".join(filter(str.isalnum, s.lower()))
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
                continue
        return True
            
        