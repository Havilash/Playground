# https://youtu.be/iSNsgj1OCLA
import random

def random_solve():
    def choose(my_num):
        nums = random.sample(range(1, 101), 50)
        return any(boxes[num] == my_num for num in nums)

    return all(choose(i) for i in range(1, 101))

def cycle_solve():
    def choose(my_num):
        num = my_num
        for _ in range(50):
            if boxes[num] == my_num:
                return True
            num = boxes[num]
        return False

    return all(choose(i) for i in range(1, 101))

trials = 5000
random_successes = 0
row_successes = 0
for _ in range(trials):
    boxes = dict(zip(range(1, 101), random.sample(range(1, 101), 100)))
    if random_solve():
        random_successes += 1
    if cycle_solve():
        row_successes += 1

print(f"Random strategy success percentage: {random_successes/trials * 100}%")
print(f"Cycle strategy success percentage: {row_successes/trials * 100}%")