class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2  # Если есть хотябы один из элементов он вернётся
