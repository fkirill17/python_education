def numEquivDominoPairs(dominoes):
    dct = {}
    out = 0
    for domino in dominoes:
        x = (min(domino), max(domino))
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1
    for i in dct:
        rep_cnt = dct[i]
        if rep_cnt > 1:
            out += rep_cnt * (rep_cnt - 1) // 2  # Формула комбинаторики заучить
    return out


print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  # -> 1
print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))  # -> 3