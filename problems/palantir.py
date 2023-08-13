from itertools import product


# x_1 + x_2 + ... + x_k = n 
# find every solution for given k, n where x, n are integers
def findSolutions(k, n):
    solutions = []
    for x in product(range(n+1), repeat=k):
        if sum(x) == n:
            solutions.append(x)
    return solutions

print(findSolutions(3, 5))

