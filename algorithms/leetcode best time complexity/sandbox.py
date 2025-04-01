def lengthOfLastWord(s):
    cnt = 0
    for i in s[::-1]:
        if not cnt and i == ' ':
            continue
        elif i != ' ':
            cnt += 1
        elif cnt and i == ' ':
            break
    return cnt


print(lengthOfLastWord("   fly me   to   the moon  "))
