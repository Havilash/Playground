import math
from re import I

def symmetric_differences(*args):
    sym = args[0]
    for i in range(1, len(args)):
        sym = sym ^ args[i]
    return sym
        
# print(symmetric_differences({1, 2, 3}, {2, 3, 4}, {2, 3}))


def multiplesOf3and5(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# print(multiplesOf3and5(1000))


def fiboEvenSum(num):
    def getFibo(n):
        n1 = 1
        n2 = 1
        fib = []
        for _ in range(n):
            fib.append(n1)
            n1, n2 = n2, n1 + n2
        return fib

    fibs = getFibo(num)
    sum = 0
    for fib in fibs:
        if fib % 2 == 0:
            sum += fib

    return sum

# print(fiboEvenSum(34))


def largestPrimeFactor(num):
    def isPrime(n):
        for i in range(2, n):
                if n%i == 0:
                    return False
        return True

    f=2  # factors
    max = 0

    while f < num:
        if num % f == 0:
            if isPrime(f):
                max = f
        f += 1
    return max

# print(largestPrimeFactor(13195))

def largestPalindromeProduct(n):
    def isPalindromic(num):
        str_num = str(num)
        if str_num == str_num[::-1]:
            return True
        return False
        
    lNum = 10**n-1  # largest n digit num
    sNum = 10**(n-1)  # smalest n digit num

    pDigits = n*2  # Plaindrome number of digits
    lPNum = 10**pDigits-1
    sPNum = 10**(pDigits-1)

    potencialP = 0  # potencial palindrome
    for i in range(lPNum, sPNum, -1):
        if isPalindromic(i):
            potencialP = i
            for i in range(lNum, sNum, -1):
                if potencialP%i == 0 and len(str(int(potencialP/i)))==n:
                    return (i, potencialP/i, potencialP)
    
# print(largestPalindromeProduct(50))


def smallestMult(n):
    def egcd(a, b):
        if a==0: return b
        if b==0: return a
        r = a%b
        return egcd(b, r)

    def lcm(a, b):
        return int(a*b)/egcd(a,b)

    maxLcm = 1
    for i in range(2, n+1):
        maxLcm = lcm(maxLcm, i)
    return maxLcm


# print(smallestMult(20))


def sumSquareDifference(n):
    sumOfN = (n*(n+1))/2
    sumOfNSquare = (n*(n+1)*(2*n+1))/6

    return (sumOfN**2) - sumOfNSquare

# print(sumSquareDifference(100))

def nthPrime(n):
    def isPrime(n):
        for i in range(2, int(n/2+1)):
                if n%i == 0:
                    return False
        return True

    i=0
    prime = 1
    while i!=n:
        prime += 1
        if isPrime(prime):
            i += 1
    return prime

# print(nthPrime(10001))


def largestProductinaSeries(n):
    thousandDigits = [7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,3,4,9,1,9,4,9,3,4,9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,9,8,4,8,0,1,8,6,9,4,7,8,8,5,1,8,4,3,8,5,8,6,1,5,6,0,7,8,9,1,1,2,9,4,9,4,9,5,4,5,9,5,0,1,7,3,7,9,5,8,3,3,1,9,5,2,8,5,3,2,0,8,8,0,5,5,1,1,1,2,5,4,0,6,9,8,7,4,7,1,5,8,5,2,3,8,6,3,0,5,0,7,1,5,6,9,3,2,9,0,9,6,3,2,9,5,2,2,7,4,4,3,0,4,3,5,5,7,6,6,8,9,6,6,4,8,9,5,0,4,4,5,2,4,4,5,2,3,1,6,1,7,3,1,8,5,6,4,0,3,0,9,8,7,1,1,1,2,1,7,2,2,3,8,3,1,1,3,6,2,2,2,9,8,9,3,4,2,3,3,8,0,3,0,8,1,3,5,3,3,6,2,7,6,6,1,4,2,8,2,8,0,6,4,4,4,4,8,6,6,4,5,2,3,8,7,4,9,3,0,3,5,8,9,0,7,2,9,6,2,9,0,4,9,1,5,6,0,4,4,0,7,7,2,3,9,0,7,1,3,8,1,0,5,1,5,8,5,9,3,0,7,9,6,0,8,6,6,7,0,1,7,2,4,2,7,1,2,1,8,8,3,9,9,8,7,9,7,9,0,8,7,9,2,2,7,4,9,2,1,9,0,1,6,9,9,7,2,0,8,8,8,0,9,3,7,7,6,6,5,7,2,7,3,3,3,0,0,1,0,5,3,3,6,7,8,8,1,2,2,0,2,3,5,4,2,1,8,0,9,7,5,1,2,5,4,5,4,0,5,9,4,7,5,2,2,4,3,5,2,5,8,4,9,0,7,7,1,1,6,7,0,5,5,6,0,1,3,6,0,4,8,3,9,5,8,6,4,4,6,7,0,6,3,2,4,4,1,5,7,2,2,1,5,5,3,9,7,5,3,6,9,7,8,1,7,9,7,7,8,4,6,1,7,4,0,6,4,9,5,5,1,4,9,2,9,0,8,6,2,5,6,9,3,2,1,9,7,8,4,6,8,6,2,2,4,8,2,8,3,9,7,2,2,4,1,3,7,5,6,5,7,0,5,6,0,5,7,4,9,0,2,6,1,4,0,7,9,7,2,9,6,8,6,5,2,4,1,4,5,3,5,1,0,0,4,7,4,8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1,1,6,4,2,7,1,7,1,4,7,9,9,2,4,4,4,2,9,2,8,2,3,0,8,6,3,4,6,5,6,7,4,8,1,3,9,1,9,1,2,3,1,6,2,8,2,4,5,8,6,1,7,8,6,6,4,5,8,3,5,9,1,2,4,5,6,6,5,2,9,4,7,6,5,4,5,6,8,2,8,4,8,9,1,2,8,8,3,1,4,2,6,0,7,6,9,0,0,4,2,2,4,2,1,9,0,2,2,6,7,1,0,5,5,6,2,6,3,2,1,1,1,1,1,0,9,3,7,0,5,4,4,2,1,7,5,0,6,9,4,1,6,5,8,9,6,0,4,0,8,0,7,1,9,8,4,0,3,8,5,0,9,6,2,4,5,5,4,4,4,3,6,2,9,8,1,2,3,0,9,8,7,8,7,9,9,2,7,2,4,4,2,8,4,9,0,9,1,8,8,8,4,5,8,0,1,5,6,1,6,6,0,9,7,9,1,9,1,3,3,8,7,5,4,9,9,2,0,0,5,2,4,0,6,3,6,8,9,9,1,2,5,6,0,7,1,7,6,0,6,0,5,8,8,6,1,1,6,4,6,7,1,0,9,4,0,5,0,7,7,5,4,1,0,0,2,2,5,6,9,8,3,1,5,5,2,0,0,0,5,5,9,3,5,7,2,9,7,2,5,7,1,6,3,6,2,6,9,5,6,1,8,8,2,6,7,0,4,2,8,2,5,2,4,8,3,6,0,0,8,2,3,2,5,7,5,3,0,4,2,0,7,5,2,9,6,3,4,5,0]
    
    maxProd = 0
    for j in range(len(thousandDigits)-n):
        prod = 1
        for i in range(n):
            prod *= thousandDigits[j+i]
        if prod > maxProd:
            maxProd = prod
    return maxProd

# print(largestProductinaSeries(13))


def specialPythagoreanTriplet(n):
    for a in range(1, n):
        for b in range(a+1, n):
            c = math.sqrt(a**2 + b**2)

            if a + b + c == n: return (a, b, c, n, a*b*c)

# print(specialPythagoreanTriplet(1000))


def primeSummation(n):
    def isPrime(n):
        for i in range(2, int(n/2+1)):
                if n%i == 0:
                    return False
        return True

    primes = []
    num = 2
    for i in range(2, n):
        if i%2!=0:
            if isPrime(i): primes.append(i)

    sum = 0 
    for prime in primes: sum += prime

    return (primes, sum)
        
# print(primeSummation(140759))


def largestGridProduct(arr):
    maxProd = 0
    crntProd = 0

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            limit = len(arr[y]) - 3

            if x < limit:
                crntProd = arr[y][x]*arr[y][x+1]*arr[y][x+2]*arr[y][x+3]
                if crntProd > maxProd: maxProd = crntProd

            if y < limit:
                crntProd = arr[y][x]*arr[y+1][x]*arr[y+2][x]*arr[y+3][x]
                if crntProd > maxProd: maxProd = crntProd

            if x < limit and y < limit:
                crntProd = arr[y][x]*arr[y+1][x+1]*arr[y+2][x+2]*arr[y+3][x+3]
                if crntProd > maxProd: maxProd = crntProd

            if x > 3 and y < limit:
                crntProd = arr[y][x]*arr[y+1][x-1]*arr[y+2][x-2]*arr[y+3][x-3]
                if crntProd > maxProd: maxProd = crntProd

    return maxProd



grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

testGrid = [[40, 17, 81, 18, 57],
            [74, 4, 36, 16, 29],
            [36, 42, 69, 73, 45],
            [51, 54, 69, 16, 92],
            [7, 97, 57, 32, 16]]

# print(largestGridProduct(grid))


def simpleDivisibleTriangleNumber(n):
    triangleNum = 0
    num = 0
    divisors = 0
    while divisors < n:
        num += 1
        triangleNum += num
        divisors = 0
        for d in range(1, triangleNum+1):
            if triangleNum % d == 0:
                divisors +=1
    return triangleNum

# print(simpleDivisibleTriangleNumber(167))


def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def divisibleTriangleNumber(n):
    triangleNum = 0
    num = 0
    numDivisors = 1
    while numDivisors < n:
        num += 1
        triangleNum += num
        factors = get_prime_factors(triangleNum)
        numDivisors = 1
        for i in list(set(factors)):
            numDivisors *= factors.count(i) + 1


    return triangleNum

# print(divisibleTriangleNumber(7947))


def largeSum(arr):
    pass    

testNums = [
  '37107287533902102798797998220837590246510135740250',
  '46376937677490009712648124896970078050417018260538'
]

# print(largeSum(testNums))


def longestCollatzSequence(limit):
    lenLongestColl = 0
    longestColl = 0
    for i in range(1, limit):
        n = i
        lenColl = 0
        while n != 1:
            lenColl += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1

        if lenColl > lenLongestColl:
            lenLongestColl = lenColl
            longestColl = i
    
    return longestColl

# print(longestCollatzSequence(100000))


def latticePaths(gridSize):
    gridSize = gridSize + 1
    grid = [[1 for _ in range(gridSize)] for _ in range(gridSize)]
    for y in range(1, gridSize):
        for x in range(1, gridSize):
            grid[x][y] = grid[x][y-1] + grid[x-1][y]
    for g in grid: print(g)
    return grid[-1][-1]

# print(latticePaths(20))


def powerDigitSum(exponent):
    num = 2**exponent
    nums = list(map(lambda x: int(x), list(str(num))))
    return sum(nums)

# print(powerDigitSum(1000))



def numberLetterCounts(limit):
    def convert(num):
        units = ("", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen ")
        tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")
        oom = ('thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion')

        if num < 0:
            return "minus " + convert(-num)

        if num < 20:
            return units[num]

        if num < 100:
            return tens[num // 10] + units[num % 10]

        if num < 10 ** 3:
            return units[num // 10 ** 2] + "hundred " + convert(num % 10 ** 2)

        for idx, name in enumerate(oom):
            scale = (idx + 1) * 3
            cap = scale + 3
            if num < 10 ** cap:
                return convert(num // 10 ** scale) + name + " " + convert(num % 10 ** scale)

        return "function " + convert.__name__ + " has exhausted its vocabulary"

    text = ""
    for i in range(limit+1):
        text += convert(i)

    return (text, len(text.replace(" ", "")))

# print(numberLetterCounts(1000))


def maximumPathSumI(t):
  for i in range(len(t)-2, 0-1, -1):
    for j in range(i+1):
      t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])
  return testTriangle[0][0]

testTriangle = [[3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3]]
[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23]
]

print(maximumPathSumI(testTriangle))