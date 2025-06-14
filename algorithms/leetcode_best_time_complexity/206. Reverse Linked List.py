def reverseList(head):
    prev = None  # Изначально предыдущего элемента нет.
    curr = head  # Начинаем с головы исходного списка.

    while curr:
        nxt = curr.next  # Сохраняем ссылку на следующий элемент.
        curr.next = prev  # Разворачиваем ссылку текущего элемента назад.
        prev = curr  # Сдвигаем на 1 ступень.
        curr = nxt  # Сдвигаем на 1 ступень.

    return prev