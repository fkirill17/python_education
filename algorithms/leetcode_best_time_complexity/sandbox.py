def lengthOfLastWord(s):
    cnt = 0
    flag = 0
    for i in s[::-1]:
        if i == ' ' and not flag:
            continue
        if i != ' ':
            cnt += 1
            flag = 1
            continue
        if i == ' ' and flag:
            break
    return cnt

print(lengthOfLastWord("   fly me   to   the moon  "))