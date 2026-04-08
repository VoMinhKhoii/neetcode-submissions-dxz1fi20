class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return True

        stack = []
        mid = len(s) // 2
        for i in range(mid):
            stack.append(s[i])
        
        for i in s[mid:]:
            curr = stack.pop()
            if curr == "{" and i != "}" or curr == "[" and i != "]" or curr != "(" and i == ")":
                return False
        return True