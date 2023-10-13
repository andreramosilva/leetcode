# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,prev_direction,leng):
            if not node:
                return leng
            if prev_direction == "left":
                left_leng = dfs(node.left,"right",leng +1)
                right_leng = dfs(node.right,"left",1)
            else:
                left_leng = dfs(node.left,"right",1)
                right_leng = dfs(node.right,"left",leng +1)
            return max(leng,left_leng,right_leng)
        return max(dfs(root,"left",0),dfs(root,"right",0)) -1
