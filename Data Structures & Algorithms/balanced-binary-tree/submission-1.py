# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root) -> int:
            
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1: return -1
            right = dfs(root.right)
            if right == -1: return -1

            # IF WE JUST RETURN -1 HERE:
            # Imagine left = -1 and right = 0.
            # abs(-1 - 0) is 1.
            # 1 > 1 is False.
            # The code thinks this node is balanced and returns 1 + max(-1, 0) = 1.
            # The "fire alarm" (-1) just got turned back into a valid height! 
            # The error was swallowed.
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1