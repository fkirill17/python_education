def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0  # Перенос
    i, j = len(a) - 1, len(b) - 1  # Индексы последних символов

    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a + bit_b + carry
        result.append(str(total % 2))  # Добавляем в результат младший бит
        carry = total // 2  # Обновляем перенос

        i -= 1
        j -= 1

    return ''.join(result[::-1])

print(addBinary("1010", "1011"))