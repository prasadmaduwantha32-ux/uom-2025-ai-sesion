def Isprime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def value_of_nth_prime(n):
    count=0
    num=1
    while count<n:
        num+=1
        if Isprime(num):
            count+=1
    return num

print(value_of_nth_prime(10001))
