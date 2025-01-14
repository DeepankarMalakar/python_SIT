import math

def combination(n, r):
    return math.comb(n, r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("C(n, r):", combination(n, r))