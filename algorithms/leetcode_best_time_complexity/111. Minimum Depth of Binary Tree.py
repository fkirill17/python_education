class Solution(object):
    def minDepth(self, root):
        if not root:  # Базовый случай: если узел пустой, глубина 0
            return 0
        left = self.minDepth(root.left)  # Рекурсивный вызов: считаем глубину левого поддерева
        right = self.minDepth(root.right)  # Рекурсивный вызов: считаем глубину правого поддерева
        if not left or not right:  # Специальная проверка
            return max(left, right) + 1
        else:  # Обычная логика
            return min(left, right) + 1
