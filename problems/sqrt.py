
def sqrt(value):
    arr = []
    a = 1
    b = value
    while abs(a - b) >= 1e-4:
        arr.append((a, b))
        a = (a + b) / 2
        b = value / a
    return arr

def sqrt(value):
    arr = []
    def rec(a, b):
        arr.append((a, b))
        if abs(a - b) < 1e-4:
            return 
        rec((a + b) / 2, value / a)
    rec(1, value)
    return arr

print(sqrt(9))