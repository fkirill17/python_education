def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0] # 'fl'
    for word in strs[1:]:  # 'flsfs'
        while not word.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix


print(longestCommonPrefix(['flsf', 'fledfw', 'flsfs']))
