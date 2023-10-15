from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root,1)])
        max_sum = root.val
        max_lvl_sum = 1

        while queue:
            temp_sum = 0
            lvl_len = len(queue)

            for _ in range(lvl_len):
                node, lvl  = queue.popleft()
                temp_sum += node.val
                
                if node.left:
                    queue.append((node.left,lvl+1))
                if node.right:
                    queue.append((node.right,lvl+1))

            if temp_sum > max_sum:
                    max_sum = temp_sum
                    max_lvl_sum = lvl
        return max_lvl_sum