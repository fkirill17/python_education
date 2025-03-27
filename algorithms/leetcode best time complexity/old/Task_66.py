def plusOne(digits: list) -> list:
    digits = digits[::-1]
    for idx in range(0, len(digits)):
        summa = digits[idx] + 1
        if summa > 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits[::-1]
    digits.append(1)
    return digits[::-1]


print(plusOne([9, 9]))
