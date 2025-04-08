class Solution:
    def firstBadVersion(n):
        l, r = 0, n
        while r > l:
            mid = (r - l) // 2 + l
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
