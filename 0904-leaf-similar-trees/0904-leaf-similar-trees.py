# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #DFS
        tree_1 = self.getleaves(root1)
        tree_2 = self.getleaves(root2)
        return tree_1 == tree_2

    def getleaves(self,root_tree):
        sequence_of_leaves =[]
        if not (root_tree):
            return sequence_of_leaves
        if root_tree.left:
            left = self.getleaves(root_tree.left)
            sequence_of_leaves.extend(left)
        if root_tree.right:
            right = self.getleaves(root_tree.right)
            sequence_of_leaves.extend(right)
        if not(root_tree.left) and not(root_tree.right):
            sequence_of_leaves.append(root_tree.val)
        return sequence_of_leaves