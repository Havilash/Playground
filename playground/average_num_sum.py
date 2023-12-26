import math
import random
from utils import decorators


@decorators.with_average(1000000)
def solution():
    num = 0
    sum = 0
    while sum < 1.0:
        num += 1
        sum += random.random()
    return num


print(f"e: {math.e}\napproximation: {solution()}")
