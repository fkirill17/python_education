def isAnagram(s, t):
    s_dct = {}
    t_dct = {}

    for i in s:
        if i in s_dct:
            s_dct[i] += 1
        else:
            s_dct[i] = 1

    for j in t:
        if j in t_dct:
            t_dct[j] += 1
        else:
            t_dct[j] = 1

    return t_dct == s_dct


print(isAnagram(s="anagram", t="nagaram"))
