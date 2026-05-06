# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(node, prev):
            nonlocal counter
            print(prev, counter)
            if node is None:
                return
            if not prev or node.val >= prev[-1]:
                prev.append(node.val)
                counter += 1
                
            dfs(node.left, prev)
            dfs(node.right, prev)
            if prev and prev[-1] == node.val:
                prev.pop()
            return
        dfs(root, [])
        return counter
            