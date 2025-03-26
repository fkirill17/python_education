import re


def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s)  # "raceacar"
    s = s.lower()
    return s == s[::-1]  # Проверка является ли полиндромом


print(isPalindrome("Race a Car"))