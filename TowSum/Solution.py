def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tb = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in tb:
            return [tb[diff], idx]
        tb[num] = idx
