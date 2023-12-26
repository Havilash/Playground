import numpy as np
from utils import timer

@timer
def quicksort(arr):
    def rec(a):
        if len(a) <= 1:
            return a
        pivot = a[0]
        left = [i for i in a[1:] if i <= pivot]
        right = [i for i in a[1:] if i > pivot]
        return rec(left) + [pivot] + rec(right)
    return rec(arr)

arr = np.random.randint(0, 1000, 1000)
quicksort(arr)
timer(arr.sort)()