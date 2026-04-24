# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # IDEA: 1 dfs to find same root value,
        # another to start traversing from it to see if it actually the same
        if not root:
            return False

        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
                
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        