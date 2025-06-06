def isBadVersion(x):
    if x >= 17:
        return True
    return False


def firstBadVersion(n):
    l, r = 0, n
    while l < r:
        mid = l + (r - l) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return l


print(firstBadVersion(22))
