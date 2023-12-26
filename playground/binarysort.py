import numpy as np
import random
from utils import timer

@timer
def binarysort(arr, n):
    def rec(a, left):
        mid = len(a) // 2
        pivot = a[mid]
        if pivot == n:
            return left + mid
        elif pivot > n:
            return rec(a[:mid], left)
        elif pivot < n:
            return rec(a[mid+1:], left + mid + 1)
    return rec(arr, 0)

arr = random.sample(range(100000), 100000)
arr.sort()
i = random.randint(0, len(arr))
n = arr[i]
found = binarysort(arr, n)
print(f"found {found}: {arr[found]}, expected {i}: {n}")