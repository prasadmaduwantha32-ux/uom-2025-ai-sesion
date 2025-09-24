def IsPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def LPF(num):
    largest_prime = None
    i = 2
    while i * i <= num:
        if num % i == 0:
            if IsPrime(i):
                largest_prime = i
            num //= i  
        else:
            i += 1
    if num > 1:  
        largest_prime = num
    return largest_prime


print(LPF(600851475143))