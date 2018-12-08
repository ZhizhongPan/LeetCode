def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sub_best = nums[0]
    best = sub_best
    for num in nums[1:]:
        if sub_best > 0:
            sub_best += num
        else:
            sub_best = num
        best =  max(best, sub_best)
        
    return sub_best
        
        