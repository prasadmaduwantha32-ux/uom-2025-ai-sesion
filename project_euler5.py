def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def GLP(num):
    lcm = 1
    for i in range(2, num + 1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm

print(GLP(20))