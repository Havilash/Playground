
# find min sum of continuous subarray
import numpy as np
from utils import timer

@timer
def min_subarray_sum(nums):
    n = len(nums)
    min_sum = float('inf')
    min_nums = []
    for i in range(n):
        for j in range(i, n+1):
            if min_sum > sum(nums[i:j]):
                min_nums = nums[i:j]
                min_sum = min(min_sum, sum(min_nums))
    return min_sum, min_nums

@timer
def min_subarray_sum_dp(nums):
    min_sum = float('inf')
    last_min = nums[0]
    for num in nums[1:]:
        min_curr = min(num + last_min, num)
        last_min = min_curr
        min_sum = min(min_curr, min_sum)
    return min_sum

arr = np.random.randint(-9, 10, 1000)
min_subarray_sum(arr)
min_subarray_sum_dp(arr)