def GetSum(n):
    if n == 0: return 0
    return n + GetSum(n - 1)


def GetLength(nums, n):
    if n == -1: return 0
    return 1 + GetLength(nums, n - 1)


def GetTail(nums, n):
    if n == len(nums) - 1: return nums[n]
    return GetTail(nums, n + 1)


def ArraysAreEqual(nums1, nums2, m, n):
    if m == -1 and n == -1: return True
    if m == -1 or n == -1: return False
    if nums1[m] != nums2[n]: return False
    return ArraysAreEqual(nums1, nums2, m - 1, n - 1)


def GetProduct(nums, n):
    if n == -1: return 1
    return nums[n] * GetProduct(nums, n - 1)


def GetFactorial(n):
    if n == 1: return 1
    return n * GetFactorial(n - 1)


def GetFibonacci(n):
    if n == 0 or n == 1: return n
    return GetFibonacci(n - 1) + GetFibonacci(n - 2)


def GetPower(base, power):  # 2^5 == 2 * 2^4  # 2 ^ 4 == 4 ^ 2
    if power == 0: return 1
    if power & 1: return base * GetPower(base, power - 1)
    return GetPower(base * base, power // 2)


def GetBinaryFormat(n):
    if n == 0: return 0
    return GetBinaryFormat(n // 2) * 10 + (n & 1)


def GetBitsCount(n):
    if n == 0: return 0
    return (n & 1) + GetBitsCount(n // 2)


def GetMin(nums, n):
    if n == -1: return 10 ** 10
    return min(nums[n], GetMin(nums, n - 1))


def Exists(nums, target, n):
    if n == -1: return False
    return nums[n] == target or Exists(nums, target, n - 1)


def GetMaxRange(nums, i, j):
    if i > j: return -10 ** 10
    return max(nums[i], GetMaxRange(nums, i + 1, j))


def GetSqrtBinarySearch(n, lo, hi):
    if lo > hi: return 0
    mi = lo + (hi - lo) / 2
    if mi * mi <= n: return max(mi, GetSqrtBinarySearch(n, mi + 0.00001, hi))
    return GetSqrtBinarySearch(n, lo, mi - 0.00001)


def IsPalindrome(s, i, j):
    if i > j: return True
    return s[i] == s[j] and IsPalindrome(s, i + 1, j - 1)


def GetReversed(nums, i, j):
    if i >= j: return [nums[i]]
    return GetReversed(nums, i + 1, j) + [nums[i]]


def GetSquared(nums, i, j):
    if i >= j: return [nums[i] * nums[i]]
    return [nums[i] * nums[i]] + GetSquared(nums, i + 1, j)


def Map(nums, n, fn):
    if n == len(nums) - 1: return [fn(nums[n])]
    return [fn(nums[n])] + Map(nums, n + 1, fn)


def Filter(nums, n, fn):
    if n == len(nums): return []
    if fn(nums[n]): return [nums[n]] + Filter(nums, n + 1, fn)
    return Filter(nums, n + 1, fn)


def Reduce(nums, n, acc, fn):
    if n == len(nums): return acc
    return Reduce(nums, n + 1, fn(acc, nums[n]), fn)


def IsTargetSumExist(nums, target):
    # Helper() helps us keep our initial function more clear and concise.
    # Helper() doesn't have nums (nums is in a closure now implicitly).
    # Helper() will have a pointer captured to the outside nums variable.
    # Therefore, we are able to pass much less variables in our recursion calls.
    # Less variables => much less stack memory is used.
    # Less variables => code is more clear.

    def Helper(n, target):
        if target == 0: return True
        if target < 0 or n < 0: return False  # Prune invalid bound conditions
        return Helper(n - 1, target) or Helper(n - 1, target - nums[n])

    return Helper(len(nums) - 1, target)


def GetAllCombinations(nums):
    ans: list[list[int]] = []

    def Helper(idx, current):
        if idx == len(nums):
            ans.append(current[:])
            return
        Helper(idx + 1, current + [nums[idx]])
        Helper(idx + 1, current)

    Helper(0, [])
    return ans


if __name__ == '__main__':
    print(GetSum(5))  # 15
    print(GetLength([1, 2, 3, 4, 5], 4))
    print(GetTail([1, 2, 3, 4, 5], 0))
    print(ArraysAreEqual([1, 2, 3, 4], [1, 2, 3, 4], 3, 3))
    print(GetProduct([1, 2, 3, 4, 5], 4))
    print(GetFactorial(5))
    print(GetFibonacci(12))
    print(GetPower(2, 15))
    print(GetBinaryFormat(134))
    print(GetBitsCount(134))
    print(GetMin([3, 4, 1, 5, 6, 7, 8, -111, 1, 3], 9))
    print(Exists([3, 4, 1, 5, 6, 7, 8, -111, 1, 3], -111, 9))
    print(GetMaxRange([3, 4, 1, 5, 6, 7, 8, -111, 1, 3], 0, 9))
    print(GetSqrtBinarySearch(17, 0, 10 ** 10))
    print(IsPalindrome("110101101101011", 0, 14))
    print(IsPalindrome("1101011011010110", 0, 15))
    print(GetReversed([1, 2, 3, 4, 5], 0, 4))
    print(GetSquared([1, 2, 3, 4, 5], 0, 4))
    print(Map([1, 2, 3, 4, 5], 0, lambda num: num * num))
    print(Filter([1, 2, 3, 4, 5], 0, lambda num: num & 1 == 1))
    print(Reduce([1, 2, 3, 4, 5], 0, 0, lambda acc, num: acc + num))
    print(IsTargetSumExist([1, 2, 3, 4, 5], 10))
    print(IsTargetSumExist([1, 2, 3, 4, 5], 17))
    print(GetAllCombinations([1, 2, 3, 4, 5]))
