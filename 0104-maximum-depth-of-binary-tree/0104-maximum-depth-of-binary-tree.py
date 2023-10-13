# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS/DFS
        if root is None:
            return 0
        # left  = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left,right) + 1
        max_dpt =0 
        stack = [(root,1)]
        while stack:
            curr_node , dpt = stack.pop(0)

            max_dpt = max(max_dpt,dpt)
            if curr_node.left:
                stack.append((curr_node.left,dpt+1))
            if curr_node.right:
                stack.append((curr_node.right,dpt+1))
            
        return max_dpt