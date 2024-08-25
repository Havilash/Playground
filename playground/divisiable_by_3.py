import random

from utils import decorators

div_by_3_nums = [0, 3, 6, 9]


def divisible_by_3(x):
    # print(x)
    if len(str(x)) <= 1:
        return x in div_by_3_nums
    return divisible_by_3(sum(map(int, list(str(x)))))


v = random.randrange(0, int(1e300))
decorators.timer(divisible_by_3)(v)
decorators.timer(lambda x: x % 3 == 0)(v)
