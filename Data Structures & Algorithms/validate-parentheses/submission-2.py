class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return True

        stack = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            if i == "]" and stack.pop() != "[" or i == ")" and stack.pop() != "(" or i == "}" and stack.pop() != "{":
                return False
        return True
