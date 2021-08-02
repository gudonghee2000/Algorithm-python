def solution(s):
    s = s[1:len(s)-1]
    nums = s.split("},")
    ret = []
    for i in range(len(nums)-1) :
        nums[i] = nums[i][1:]
    nums[len(nums)-1] = nums[len(nums)-1][1:len(nums[len(nums)-1])-1]
    nums.sort(key = lambda x : len(x))
    for n in nums :
        temp = n.split(',')
        for t in temp :
            if int(t) not in ret :
                ret.append(int(t))
    return ret
