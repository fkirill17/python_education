def longestcommonprefix(s: list):
    prefix = s[0]
    for i in s[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
    return prefix




print(longestcommonprefix(["fd", "fdk", "f211"]))