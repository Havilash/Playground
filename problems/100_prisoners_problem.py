import random
from utils import decorators

success_func = lambda success: 1 if success else 0
trials = 5000
generate_boxes = lambda: dict(zip(range(1, 101), random.sample(range(1, 101), 100)))


@decorators.with_average(trials, success_func)
def random_solve():
    boxes = generate_boxes()

    def choose(my_num):
        nums = random.sample(range(1, 101), 50)
        return any(boxes[num] == my_num for num in nums)

    return all(choose(i) for i in range(1, 101))


@decorators.with_average(trials, success_func)
def cycle_solve():
    boxes = generate_boxes()

    def choose(my_num):
        num = my_num
        for _ in range(50):
            if boxes[num] == my_num:
                return True
            num = boxes[num]
        return False

    return all(choose(i) for i in range(1, 101))


# Example usage:
random_strategy_success_percentage = random_solve()
cycle_strategy_success_percentage = cycle_solve()

print(f"Random strategy success percentage: {random_strategy_success_percentage:.2f}%")
print(f"Cycle strategy success percentage: {cycle_strategy_success_percentage:.2f}%")
