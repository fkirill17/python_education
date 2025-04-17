def numEquivDominoPairs(dominoes):
    dct = {}
    out = 0
    for i in dominoes:
        a = i[0]
        b = i[1]
        key = (min(a, b), max(a, b))  # Приведение ключей к одному виду. В качестве ключа imutable кортеж
        if key not in dct:
            dct[key] = 1
        else:
            dct[key] += 1
    for j in dct:
        x = dct[j]
        if x > 1:
            pairs = x * (x - 1) // 2  # Pair(пары) counting через комбинаторику
            out += pairs
    return out


print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  # -> 1
print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))  # -> 3
