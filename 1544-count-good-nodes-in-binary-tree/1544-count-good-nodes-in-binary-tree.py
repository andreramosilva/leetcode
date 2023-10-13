# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        return self.dfs(root,0,root.val)

    def dfs(self,root,number_of_goods,last_good):
    #def dfs(self,root):
        if (root.val >= last_good):
            last_good  = root.val
            number_of_goods+=1
        if (root.left):
            number_of_goods = self.dfs(root.left,number_of_goods,last_good)
        if (root.right):
            number_of_goods = self.dfs(root.right,number_of_goods,last_good)

        return number_of_goods