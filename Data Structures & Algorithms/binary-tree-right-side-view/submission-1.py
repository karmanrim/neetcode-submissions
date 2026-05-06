# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root, levels, level):
        if root is None:
            return
        if level == len(levels):
            levels.append(root.val)
        self.preorder(root.right, levels, level + 1)
        self.preorder(root.left, levels, level + 1)
        return 

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder(root, result, 0)
        return result