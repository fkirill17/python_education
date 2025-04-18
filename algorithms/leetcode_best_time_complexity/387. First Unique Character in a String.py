def firstUniqChar(s):
    dct = {}  # Частотный словарь (Frequency Counter)
    for symbol in s:  # Накопление всех уникальных символов в ключах словаря и количество повторений в значениях
        if symbol in dct:
            dct[symbol] += 1
        else:
            dct[symbol] = 1
    for idx, symbol2 in enumerate(s):  # Поиск первого уникального элемента
        cnt_rep = dct[symbol2]
        if cnt_rep == 1:
            return idx
    return -1
    # Частотный словарь (Frequency Counter)
    # Два прохода по данным (Two-pass Algorithm)
    # Сложность O(n)
