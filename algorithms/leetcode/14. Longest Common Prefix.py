def longestCommonPrefix(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


print(longestCommonPrefix(["flfs", "fldsls", "flalafw"]))