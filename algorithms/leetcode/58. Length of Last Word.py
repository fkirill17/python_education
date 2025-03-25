def lengthOfLastWord(s):
    k = 0
    flag = 0
    for i in s[::-1]:
        if i == ' ' and not flag:
            continue
        elif i != ' ':
            flag = 1
            k += 1
        elif i == ' ' and flag:
            break
    return k


print(lengthOfLastWord("fdsfa fsafdf safas  "))