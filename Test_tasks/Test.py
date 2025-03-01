def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for x in strs[1:]:
        while not x.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix






print(longestCommonPrefix(['flsf', 'fledfw', 'flsfs']))  # -> 'fl'
