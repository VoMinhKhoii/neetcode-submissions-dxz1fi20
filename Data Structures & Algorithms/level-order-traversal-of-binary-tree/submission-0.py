# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 

        res = []
        nodeQueue = []
        currLevel = []

        if not root:
            return res

        res.append([root.val])
        
        nodeQueue.append(root)

        while nodeQueue:
            for i in range(len(nodeQueue)):
                curr = nodeQueue.pop(0)
                if curr.left: 
                    currLevel.append(curr.left.val)
                    nodeQueue.append(curr.left)
                if curr.right:
                    currLevel.append(curr.right.val)
                    nodeQueue.append(curr.right)
            if currLevel:
                res.append(currLevel)
            currLevel = []
        return res