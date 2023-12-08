from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__!r} executed in {(total_time):.4f}s")
        return result

    return wrapper


def with_average(trials, value_func=lambda x: x):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            total_value = 0
            for _ in range(trials):
                result = func(*args, **kwargs)
                total_value += value_func(result)
            return total_value / trials

        return inner

    return wrapper
