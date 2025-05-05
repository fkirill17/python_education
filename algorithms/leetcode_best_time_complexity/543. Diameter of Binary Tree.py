def diameterOfBinaryTree(self, root):
    self.out = 0

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        self.out = max(self.out, left + right)
        return max(left, right) + 1

    dfs(root)
    return self.out