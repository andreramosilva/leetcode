# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ctr =0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # return self.dfs(root)
        if not(root):
            return 0
        self.psh(root,targetSum,0)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)

        return self.ctr


    def psh(self,node,s, curr_sum):
            if node == None:
                return 
            curr_sum += node.val
            if (curr_sum == s):
                self.ctr+=1
            self.psh(node.left,s,curr_sum)
            self.psh(node.right,s,curr_sum)


        