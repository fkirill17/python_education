class Solution(object):
    def maxDepth(self, root):
        if not root:  # Базовый случай: если узел пустой, глубина 0
            return 0
        left = self.maxDepth(root.left)  # Рекурсивный вызов: считаем глубину левого поддерева
        right = self.maxDepth(root.right)  # Рекурсивный вызов: считаем глубину правого поддерева
        return max(left, right) + 1  # Берем максимум глубин и прибавляем 1 (учитываем текущий узел)


