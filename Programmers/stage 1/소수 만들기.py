def chk(i, j, t):
    num = i + j + t
    for ch in range(2, num):
        if num % ch == 0:
            return False
    return True


def solution(nums):
    ret = 0
    nums.sort()

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for t in range(j + 1, len(nums)):
                if chk(nums[i], nums[j], nums[t]):
                    ret += 1

    return ret
