class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        stack = []
        mapping = { "}" : "{", 
                    "]" : "[",
                    ")" : "("}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                topElement = stack.pop() if stack else "0"
                if topElement != mapping[i]:
                    return False
        return len(stack) == 0
