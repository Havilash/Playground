from itertools import product

def every_combination(num, b):
    digits = []
    for _ in range(b):
        digits.append(int(num % b))
        num //= b
    return digits[::-1]

# x_1 + x_2 + ... + x_k = n 
# find every solution for given k, n where x, n are integers
def findSolutions(k, n):
    solutions = []
    loop = [every_combination(i, n+1) for i in range((n+1) ** k)]
    print(loop)
    for x in product(range(n+1), repeat=k):
        if sum(x) == n:
            solutions.append(x)
    return solutions

print(findSolutions(3, 6))

