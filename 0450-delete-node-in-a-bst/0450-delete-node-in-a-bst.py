# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_val = self.find_min(root.right)
            root.val = min_val
            root.right = self.deleteNode(root.right,min_val)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            root.left = self.deleteNode(root.left,key)
        return root




    def find_min(self, node):
        while node.left:
            node = node.left
        return node.val