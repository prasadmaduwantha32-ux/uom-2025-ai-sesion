def ISprime(num):
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
                 return 0
    else:
        return 1

def sum_of_below_prime(num):
    psum=0
    for  x in range(2,num):
        if ISprime(x)==1:
            psum+=x
    return psum



print(sum_of_below_prime(2000000))