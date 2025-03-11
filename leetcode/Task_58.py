def lengthOfLastWord(s):
    lst_1 = list(s)
    lst_1 = lst_1[::-1]
    lst_1.append(" ")
    lst_2 = []
    for symbol in lst_1:
        if symbol != " ":
            lst_2.append(symbol)
        if lst_2 != [] and symbol == " ":
            return len(lst_2)


print(lengthOfLastWord("a aaa aaaaa  "))
