def Sum_F_sum(num):
    if num < 2:
        return 0
    a=1
    b=2
    sum=0
    while b<=num:
        if b%2==0:
            sum+=b
        a,b=b,a+b
    return sum

print(Sum_F_sum(4000000))